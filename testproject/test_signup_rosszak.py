import randomstring
import locators
import classok
import pytest

lap = classok.test_Sign_upLap()
assert lap.test_01_rossz_mezok("", "", "", locators.userhiba[0])
lap = classok.test_Sign_upLap()
assert lap.test_01_rossz_mezok(randomstring.nev(), "", "", locators.userhiba[1])
lap = classok.test_Sign_upLap()
assert lap.test_01_rossz_mezok(randomstring.nev(), randomstring.emil(), "", locators.userhiba[2])
lap = classok.test_Sign_upLap()
assert lap.test_01_rossz_mezok(randomstring.nev(), randomstring.emil(), "", locators.userhiba[2])
lap = classok.test_Sign_upLap()
assert lap.test_01_rossz_mezok(randomstring.nev(), randomstring.emil(), randomstring.name(), locators.userhiba[3])


