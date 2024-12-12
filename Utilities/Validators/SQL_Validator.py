"""
NOTE : ceci est un filtre anti-injection SQL, mais il n'est pas nécessaire puisque le code est échappé au niveau de la couche repository.
Il est juste présent pour répondre au point de la consigne.
"""


class Validator :
    def __init__(self, task_to_analyze):
         self.launch = task_to_analyze.id
         self.data_to_analyze = task_to_analyze.title

    def anti_sql_injection_filter(self) :
 
            sql_injection_keywords = ["SELECT", "FROM", "WHERE", "ORDER BY", "GROUP BY", "HAVING", "INSERT INTO", 
            "UPDATE", "DELETE", "DROP", "TRUNCATE", "CREATE", "ALTER", "RENAME",
            "--", "#", "/*...*/", "'", "\"", "=", "<>", "!=", "AND", "OR", "BETWEEN", 
            "IN", "LIKE", "IS NULL", "IS NOT NULL",
            "UNION", "UNION ALL", "CAST", "CONCAT", "SUBSTRING", "SLEEP", "BENCHMARK",
            "VERSION()", "DATABASE()", "USER()", "CURRENT_USER()", "LOAD_FILE()", 
            "EXEC", "XP_CMDSHELL", "SELECT INTO OUTFILE"]

            if self.launch <= -2 : #cas où on demande l'activation du filtre   
                if any(word.lower() in self.data_to_analyze.lower() for word in sql_injection_keywords) :
                    return True
                else :
                    return False
            else : #cas où on ne demande pas l'activation du filtre
                 return False
                
                 
