#!/usr/bin/env python


from re_patterns import Rstr
import pytest


def test_add():
    assert Rstr("hello") + Rstr("world") == "helloworld"
    assert Rstr("hello") + "world" == "helloworld"
    assert "hello" + Rstr("world") == "helloworld"


def test_named():
    r = Rstr("this").named("group_name")
    assert r == "(?P<group_name>this)"


def test_named_optional():
    r = Rstr("this").named("group_name", optional=True)
    assert r == "(?P<group_name>this)?"


def test_followed_by():
    r = Rstr("this").followed_by("that")
    assert r == "this(?=that)"


def test_not_followed_by():
    r = Rstr("this").not_followed_by("that")
    assert r == "this(?!that)"


def test_preceded_by():
    r = Rstr("this").preceded_by("that")
    assert r == "(?<=that)this"


def test_not_preceded_by():
    r = Rstr("this").not_preceded_by("that")
    assert r == "(?<!that)this"


def test_no_capture():
    r = Rstr("this").no_capture()
    assert r == "(?:this)"


def test_group():
    r = Rstr("this").group()
    assert r == "[this]"


def test_unnamed():
    r = Rstr("this").unnamed()
    assert r == "(this)"


def test_unnamed_optional():
    r = Rstr("this").unnamed(optional=True)
    assert r == "(this)?"


def test_comment():
    r = Rstr("this").comment()
    assert r == "(?#this)"


def test_append():
    r = Rstr("this").append("that")
    assert r == "thisthat"


def test_prepend():
    r = Rstr("this").prepend("that")
    assert r == "thatthis"


def test_join():
    r = Rstr("this").join("that", "something", "other")
    assert r == "thisthatsomethingother"


def test_or():
    assert "this|that" == Rstr("this") | Rstr("that")
    assert "this|that" == Rstr("this") | "that"
    with pytest.raises(TypeError, match=r"unsupported operand type\(s\)"):
        "this" | Rstr("that")


def test_compile():
    r = Rstr(r"this.\n").compile(Rstr.re.DOTALL | Rstr.re.MULTILINE)
    assert r == Rstr.re.compile(r"this.\n", flags=Rstr.re.DOTALL | Rstr.re.MULTILINE)


def test_match():
    m = Rstr(r"this.\n").match(r"this\n\n", flags=Rstr.re.DOTALL)
    assert m


