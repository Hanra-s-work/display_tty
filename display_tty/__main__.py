from src import Disp, TOML_CONF


if __name__ == "__main__":
    DI = Disp(
        toml_content=TOML_CONF,
        save_to_file=False,
        file_name="test_run.tmp",
        file_descriptor=None
    )
    DI.test_the_class()
