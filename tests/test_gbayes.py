from gbayes import __version__
from gbayes.gbayes import fn_gbayes

def test_gbayes():
    assert fn_gbayes() == "Hello World"
