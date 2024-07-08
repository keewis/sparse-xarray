from importlib.metadata import version

try:
    __version__ = version("sparse_xarray")
except Exception:
    __version__ = "9999"
