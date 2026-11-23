from mochihttp.__main__ import main


def test_greet(capfd):
    main()

    out, err = capfd.readouterr()
    assert out == "I Love Mochi!!!\n"
