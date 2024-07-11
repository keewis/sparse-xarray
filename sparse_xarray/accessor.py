import xarray as xr


@xr.register_dataarray_accessor("sparse")
class SparseXarray:
    def __init__(self, obj):
        self.obj = obj

    @property
    def nnz(self):
        return self.obj.data.nnz

    @property
    def format(self):
        pass

    @property
    def as_dense(self):
        return self.obj.as_numpy()

    def as_format(self, format):
        pass

    @property
    def fill_value(self):
        pass
