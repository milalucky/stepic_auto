
# вариант с функцией

# def test_input_text(expected_result, actual_result):
#     assert expected_result == actual_result, f"Ожидаем {expected_result}, Получаем {actual_result}"
#
# expected_result = int(input())
# actual_result = int(input())
#
# test_input_text(expected_result, actual_result)


# вариант без функции
expected_result = int(input())
actual_result = int(input())

assert expected_result == actual_result, f"Ожидаем {expected_result}, Получаем {actual_result}"