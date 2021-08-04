import randomstring
import lokatorok
import classok

lap = classok.TestSign_upLap()
assert lap.test_01_rossz_mezok("", "", "", lokatorok.userhiba[0])
lap = classok.TestSign_upLap()
assert lap.test_01_rossz_mezok(randomstring.nev(), "", "", lokatorok.userhiba[1])
lap = classok.TestSign_upLap()
assert lap.test_01_rossz_mezok(randomstring.nev(), randomstring.emil(), "", lokatorok.userhiba[2])
lap = classok.TestSign_upLap()
assert lap.test_01_rossz_mezok(randomstring.nev(), randomstring.emil(), "", lokatorok.userhiba[2])
lap = classok.TestSign_upLap()
assert lap.test_01_rossz_mezok(randomstring.nev(), randomstring.emil(), randomstring.name(), lokatorok.userhiba[3])
