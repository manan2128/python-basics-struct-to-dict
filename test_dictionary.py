import unittest

from dictionary import Student, student_to_dict


class ConversionTests(unittest.TestCase):
    def test_converts_record_fields(self):
        self.assertEqual(
            student_to_dict(Student("Example", 10, 90.99)),
            {"name": "Example", "roll": 10, "marks": 90.99},
        )

    def test_result_is_independent_of_record(self):
        record = Student("Example", 1, 0)
        converted = student_to_dict(record)
        converted["marks"] = 100
        self.assertEqual(record.marks, 0)


if __name__ == "__main__":
    unittest.main()
