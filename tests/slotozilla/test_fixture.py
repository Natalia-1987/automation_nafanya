def test_fixture(logger_fixture, driver_google):
    assert "google" in driver_google
    log = logger_fixture
    log.info("test_fixture - ok")
