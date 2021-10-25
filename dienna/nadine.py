import enum


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

    base_url = 'https://office.kemenkeu.go.id/api'

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
        endpoint = self.get_endpoint('/AmplopNd')
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
        endpoint = self.get_endpoint('/AmplopNd/NdArsipOptimized')
        return self.get_amplop_nd(endpoint, search, filter_, urgensi, reset, tag, type_, unit, start_date, end_date,
                                  limit, offset, raw)
