import pytest

from com.redhat.tssc import TSSCException

def raise_TSSCException():
    raise TSSCException('test')

def test_TSSCException():
    with pytest.raises(TSSCException):
        raise_TSSCException()
