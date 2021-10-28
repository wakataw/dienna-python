import datetime
import enum
import time


class DocumentType(enum.Enum):
    """
    Objek referensi tipe dokumen
    """
    ALL = 'all'
    KONSEP = 'konsepNd'
    NASKAH_DINAS = 'NdKeluar'
    DISPOSISI_TERIMA = 'disposisi'


class Nadine(object):
    """
    Nadine API Wrapper
    """

    base_url = 'https://office.kemenkeu.go.id'

    def __init__(self, session):
        """
        Object constructor
        :param session: requests session object
        """
        self.__session = session

    def get_endpoint(self, endpoint):
        """
        Endpoint url factory
        :param endpoint: API endpoint
        :return: Full API Endpoint URL
        """
        return self.base_url + endpoint

    def get_user_info(self):
        """
        Get user info
        :return: User Data
        """
        return self.__session.get(
            self.get_endpoint('/Index/UserInfo')
        ).json()

    def get_config_data(self):
        """
        Get user configuration data
        :return:
        """
        return self.__session.get(
            self.get_endpoint('/Index/GetConfigData')
        ).json()

    def get_notifications(self, limit=10, offset=0):
        """
        Get nadine notification
        :param limit: data paging limit
        :param offset: data paging offset
        :return: list of notification
        """
        return self.__session.get(
            self.get_endpoint('/api/RefFaq/Notifikasi'),
            params={
                'limit': limit,
                'offset': offset,
            }
        ).json()

    def get_sticky_message(self, limit=10, offset=0):
        """
        Get nadine sticky message
        :param limit: data paging limit
        :param offset: data paging offset
        :return: list of sticky message
        """
        return self.__session.get(
            self.get_endpoint('/Index/GetStickyMessage'),
            params={
                'limit': limit,
                'offset': offset,
            }
        )

    @property
    def version(self):
        """
        Get application version, commit message, env, and version hash
        :return:
        """
        return self.__session.get(
            self.get_endpoint('/api/Versi/versi')
        ).json()

    def get_tag(self):
        """
        Get all generated tag
        :return: list of tags
        """
        return self.__session.get(
            self.get_endpoint('/api/refTagnd')
        ).json()

    def get_amplop_nd(self, endpoint, search=None, filter_=None, urgensi='All', reset=False, tag=None, type_=DocumentType.ALL,
                   unit=None, start_date=None, end_date=None, limit=15, offset=0, raw=False):
        """
        API Endpoint untuk menu Mejaku/Arsip
        Endpoint: https://office.kemenkeu.go.id/api/AmplopNd

        :param search: Kata kunci pencarian
        :param filter_: Belum diketahui, tidak ada menu yang menghaislkan parameter ini
        :param urgensi: Urgensi surat, tidak ada menu yang menghasilkan parameter ini
        :param reset: Reset hasil pencarian jika sebelumnya sudah diterapkan filter
        :param tag: Filter pencarian berdasarkan tag nota dinas
        :param type_: Filter pencarian berdasarkan tipe dokumen, referensi type gunakan object DocumentType
        :param unit: Filter pencarian berdasarkan unit, tidak ada menu yang menghasilkan parameter ini
        :param start_date: Filter pencarian berdasarkan tanggal setelah atau sama dengan start date
        :param end_date: Filter pencarian surat sebelum atau sama dengan tanggal end_date
        :param limit: Limit result
        :param offset: Offset result
        :return: Dict atau Raw Requests respon jika raw == True
        """
        resp = self.__session.get(
            endpoint,
            params={
                'search': search,
                'filter': filter_,
                'urgensi': urgensi,
                'reset': reset,
                'tagnd': tag,
                'type': type_,
                'UnitFilter': unit,
                'StartDateFilter': start_date,
                'EndDateFilter': end_date,
                'limit': limit,
                'offset': offset,
            }
        )

        if not raw:
            return resp.json()

        return resp

    def get_mejaku(self, search=None, filter_=None, urgensi='All', reset=False, tag=None, type_=DocumentType.ALL,
                   unit=None, start_date=None, end_date=None, limit=15, offset=0, raw=False):
        """
        API Endpoint untuk menu Mejaku
        Endpoint: https://office.kemenkeu.go.id/api/AmplopNd

        :param search: Kata kunci pencarian
        :param filter_: Belum diketahui, tidak ada menu yang menghaislkan parameter ini
        :param urgensi: Urgensi surat, tidak ada menu yang menghasilkan parameter ini
        :param reset: Reset hasil pencarian jika sebelumnya sudah diterapkan filter
        :param tag: Filter pencarian berdasarkan tag nota dinas
        :param type_: Filter pencarian berdasarkan tipe dokumen, referensi type gunakan object DocumentType
        :param unit: Filter pencarian berdasarkan unit, tidak ada menu yang menghasilkan parameter ini
        :param start_date: Filter pencarian berdasarkan tanggal setelah atau sama dengan start date
        :param end_date: Filter pencarian surat sebelum atau sama dengan tanggal end_date
        :param limit: Limit result
        :param offset: Offset result
        :return: Dict atau Raw Requests respon jika raw == True
        """
        endpoint = self.get_endpoint('/api/AmplopNd')
        return self.get_amplop_nd(endpoint, search, filter_, urgensi, reset, tag, type_, unit, start_date, end_date,
                                  limit, offset, raw)

    def get_arsip(self, search=None, filter_=None, urgensi='All', reset=False, tag=None, type_=DocumentType.ALL,
                   unit=None, start_date=None, end_date=None, limit=15, offset=0, raw=False):
        """
        API Endpoint untuk menu Arsip
        Endpoint: https://office.kemenkeu.go.id/api/AmplopNd/NdArsipOptimized

        :param search: Kata kunci pencarian
        :param filter_: Belum diketahui, tidak ada menu yang menghaislkan parameter ini
        :param urgensi: Urgensi surat, tidak ada menu yang menghasilkan parameter ini
        :param reset: Reset hasil pencarian jika sebelumnya sudah diterapkan filter
        :param tag: Filter pencarian berdasarkan tag nota dinas
        :param type_: Filter pencarian berdasarkan tipe dokumen, referensi type gunakan object DocumentType
        :param unit: Filter pencarian berdasarkan unit, tidak ada menu yang menghasilkan parameter ini
        :param start_date: Filter pencarian berdasarkan tanggal setelah atau sama dengan start date
        :param end_date: Filter pencarian surat sebelum atau sama dengan tanggal end_date
        :param limit: Limit result
        :param offset: Offset result
        :return: Dict atau Raw Requests respon jika raw == True
        """
        endpoint = self.get_endpoint('/api/AmplopNd/NdArsipOptimized')
        return self.get_amplop_nd(endpoint, search, filter_, urgensi, reset, tag, type_, unit, start_date, end_date,
                                  limit, offset, raw)

    def download_signed_document(self, doc_id, doc_signature, chunk_size=1024*100):
        """
        Download signed document blob
        https://office.kemenkeu.go.id/api/Dokumen/DownloadSigned/12787137/49aa7dc014854cdca3ac967b93080d4d
        :param doc_id: Document ID
        :param doc_signature: Document Signature Hash
        :param chunk_size: Document download buffer size in bytes
        :return: Document Bytes Generator
        """
        endpoint = '{}/{}/{}'.format(
            self.get_endpoint('/api/Dokumen/DownloadSigned'),
            doc_id,
            doc_signature
        )
        resp = self.__session.get(
            endpoint,
            stream=True,
        )

        for chunk in resp.iter_content(chunk_size=chunk_size):
            yield chunk

    def mark_as_read(self, *amplop_ids):
        """
        Mark document as read
        /api/Disposisi/UpdateStatus/1
        :param amplop_ids: list of amplop id to update
        :return: amplop status
        """
        return self.__session.patch(
            self.get_endpoint('/api/Disposisi/UpdateStatus/1'),
            json=amplop_ids
        ).json()

    def get_document_detail(self, doc_id, sender_id):
        """
        Get document detail (detil button)
        :param doc_id: document id
        :param sender_id: document sender id
        :return: document information detail
        """

        return self.__session.get(
            self.get_endpoint('/api/NdKeluars/NdDataDetail/'+str(doc_id)),
            params={
                'pengirimId': sender_id
            }
        ).json()

    def get_document_no(self, doc_id):
        """
        Get document number
        :param doc_id: document id
        :return: document number information
        """
        return self.__session.get(
            self.get_endpoint('/api/NdKeluars/GetNomorNd/'+str(doc_id))
        ).json()

    def get_document_type_ref(self):
        """
        Get document type reference
        :return:
        """
        return self.__session.get(
            self.get_endpoint('/api/RefJenisnds')
        ).json()

    def get_history_disposisi(self, disposisi_id, amplop_id):
        """
        Get history disposisi
        endpoint: /api/Disposisi/GetHistoryDisposisi/41348944?amplopId=107296136
        :param disposisi_id: disposisi id
        :param amplop_id: amplop id
        :return:
        """
        return self.__session.get(
            self.get_endpoint('/api/Disposisi/GetHistoryDisposisi/'+str(disposisi_id)),
            params={
                'amplopId': amplop_id
            }
        ).json()

    def set_tag(self, amplop_id, *tags):
        """
        Set amplop tag
        :param amplop_id: amplop id
        :param tags: list of tag name
        :return: amplop json object
        """
        return self.__session.patch(
            self.get_endpoint('/api/Disposisi/UpdateTag/'+str(amplop_id)),
            json=tags
        ).json()

    def create_tag(self, tag):
        """
        Create tag
        :param tag: tag name
        :return: boolean
        """
        resp = self.__session.post(
            self.get_endpoint('/api/refTagnd'),
            json={
                "IdTagnd": None,
                "UnitId": None,
                "UserId": None,
                "Name": tag,
                "CreatedAt": None,
                "UpdatedAt": None
            }
        )

        return True if resp.text.strip() == '1' else False

    def delete_tag(self, tag_id):
        """
        Delete tag by tag id
        :param tag_id: tag id
        :return: tag object
        """
        return self.__session.delete(
            self.get_endpoint('/api/refTagnd/'+str(tag_id))
        ).json()

    def get_statistik_naskah_dinas(self, tahun=datetime.datetime.now().year):
        """
        Get data statistik naskah dinas dari halaman dashboard
        :param tahun: tahun naskah dinas, default tahun berjalan
        """
        return self.__session.get(
            self.get_endpoint('/api/AmplopNd/GetTotalNdLaporan'),
            params={
                'year': tahun
            }
        ).json()

    def get_dashboard_naskah_keluar(self, tahun=datetime.datetime.now().year):
        """
        Get data statistik naskah dinas keluar dari halaman dashboard
        :param tahun: tahun naskah dinas, default tahun berjalan
        """
        return self.__session.get(
            self.get_endpoint('/api/AmplopNd/DashboardNaskahKeluar'),
            params={
                'year': tahun
            }
        ).json()

    def get_dashboard_naskah_keluar_atas_nama(self, tahun=datetime.datetime.now().year):
        """
        Get data statistik naskah dinas keluar atas nama dari halaman dashboard
        :param tahun: tahun naskah dinas, default tahun berjalan
        """
        return self.__session.get(
            self.get_endpoint('/api/AmplopNd/DashboardNaskahKeluarAtasNama'),
            params={
                'year': tahun
            }
        ).json()

    def get_dashboard_naskah_keluar_pengirim_atas_nama(self, tahun=datetime.datetime.now().year):
        """
        Get data statistik naskah dinas keluar pengirim atas nama dari halaman dashboard
        :param tahun: tahun naskah dinas, default tahun berjalan
        """
        return self.__session.get(
            self.get_endpoint('/api/AmplopNd/DashboardNaskahKeluarPengirimAtasNama'),
            params={
                'year': tahun
            }
        ).json()

    def get_dashboard_naskah_masuk(self, tahun=datetime.datetime.now().year):
        """
        Get data statistik naskah dinas masuk dari halaman dashboard
        :param tahun: tahun naskah dinas, default tahun berjalan
        """
        return self.__session.get(
            self.get_endpoint('/api/AmplopNd/DashboardNaskahMasuk'),
            params={
                'year': tahun
            }
        ).json()

    def get_dashboard_nashkah_tembusan(self, tahun=datetime.datetime.now().year):
        """
        Get data statistik naskah dinas tembusan dari halaman dashboard
        :param tahun: tahun naskah dinas, default tahun berjalan
        """
        return self.__session.get(
            self.get_endpoint('/api/AmplopNd/DashboardNaskahTembusan'),
            params={
                'year': tahun
            }
        ).json()

    def get_dashboard_naskah_disposisi_masuk(self, tahun=datetime.datetime.now().year):
        """
        Get data statistik naskah dinas disposisi masuk dari halaman dashboard
        :param tahun: tahun naskah dinas, default tahun berjalan
        """
        return self.__session.get(
            self.get_endpoint('/api/AmplopNd/DashboardNaskahDisposisiMasuk'),
            params={
                'year': tahun
            }
        ).json()

    def get_dashboard_naskah_disposisi_keluar(self, tahun=datetime.datetime.now().year):
        """
        Get data statistik naskah dinas disposisi keluar dari halaman dashboard
        :param tahun: tahun naskah dinas, default tahun berjalan
        """
        return self.__session.get(
            self.get_endpoint('/api/AmplopNd/DashboardNaskahDisposisiKeluar'),
            params={
                'year': tahun
            }
        ).json()

    def get_dashboard_naskah_draft(self, tahun=datetime.datetime.now().year):
        """
        Get data statistik draft naskah dinas dari halaman dashboard
        :param tahun: tahun naskah dinas, default tahun berjalan
        """
        return self.__session.get(
            self.get_endpoint('/api/AmplopNd/DashboardNaskahDraft'),
            params={
                'year': tahun
            }
        ).json()
