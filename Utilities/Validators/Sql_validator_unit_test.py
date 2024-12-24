import unittest
from SQL_Validator import Validator

#NOTE : ces tests unitaires sont juste là pour la consigne

class TestTask:
    """Classe Task identique à celle utilisée par le programme"""
    def __init__(self, id=None, title=None, is_done=None):
        self.id = id
        self.title = title
        self.is_done = is_done

class TestValidator(unittest.TestCase):

    def test_sql_injection_detected(self):
        """Test pour vérifier si les mots-clés d'injection SQL sont détectés"""
        task = TestTask(-2, "SELECT * FROM task WHERE id=1", 0)
        validator = Validator(task)
        self.assertTrue(validator.anti_sql_injection_filter())

    def test_sql_injection_not_detected(self):
        """Test pour vérifier qu'une requête sûre passe"""
        task = TestTask(-2, "Préparer repas", 0)
        validator = Validator(task)
        self.assertFalse(validator.anti_sql_injection_filter())

    def test_filter_not_active(self):
        """Test pour vérifier que le filtre est désactivé lorsque launch > -2"""
        task = TestTask(0, "SELECT * FROM task", 0)
        validator = Validator(task)
        self.assertFalse(validator.anti_sql_injection_filter())

    def test_empty_title(self):
        """Test pour gérer un titre vide (inutile, mais là pour le principe)"""
        task = TestTask(-2, "", 0)
        validator = Validator(task)
        self.assertFalse(validator.anti_sql_injection_filter())

    def test_not_capital_detection(self):
        """Test pour vérifier la détection des minuscules"""
        task = TestTask(-2, "select * from users", 0)
        validator = Validator(task)
        self.assertTrue(validator.anti_sql_injection_filter())

if __name__ == "__main__" :
    unittest.main()
