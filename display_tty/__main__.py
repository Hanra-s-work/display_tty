from .my_disp import Disp, TOML_CONF

if __name__ == "__main__":
    TEST_DATA = {
        "test_data1": "test_data1.1",
        "test_data2": "test_data2.1",
        "test_data3": [
            "test_data_list3.1",
            "test_data_list3.2",
            "test_data_list3.3",
            "test_data_list3.4",
            "test_data_list3.5"
        ],
        "test_data4": "test_data4.1",
        "test_data5": {
            "test_data5.1": "test_data5.1.1",
            "test_data5.2": "test_data5.2.1",
            "test_data5.3": "test_data5.3.1",
            "test_data5.4": "test_data5.4.1"
        },
        "test_data6": [
            {
                "test_data6.1": "test_data6.1.1",
                "test_data6.2": "test_data6.2.1"
            },
            [
                "test_data_list6.3.1",
                "test_data_list6.3.1",
                "test_data_list6.3.1",
                "test_data_list6.3.1"
            ]
        ],
        "test_data7": {
            "test_data7.1": {
                "test_data7.1.1": "test_data7.1.1.1",
                "test_data7.1.2": "test_data7.1.2.1"
            },
            "test_data7.2": [
                "test_data7.2.1",
                "test_data7.2.2",
                "test_data7.2.3",
                "test_data7.2.4",
                "test_data7.2.5"
            ]
        }
    }
    DI = Disp(
        TOML_CONF,
        False,
        "test_run.tmp"
    )
    DI.append_run_date()
    DI.animate_message("Test Message !", 0.01)
    DI.error_message("Test Error !")
    DI.inform_message("Test Inform !")
    DI.success_message("Test Success !")
    DI.warning_message("Test Warning !")
    DI.question_message("Test Question !")
    DI.title("Test title")
    DI.sub_title("Test sub title")
    DI.sub_sub_title("Test sub sub title")
    DI.tree("Test data", TEST_DATA)
    DI.close_file()
