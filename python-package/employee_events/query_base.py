# Import any dependencies needed to execute SQL queries
import pandas as pd
from employee_events.sql_execution import QueryMixin

# Define a class called QueryBase
# Use inheritance to add methods for querying the employee_events database
class QueryBase:

    # Class attribute to specify context: either 'employee' or 'team'
    name = ""

    # Placeholder for a method to return list of names (override in subclasses)
    def names(self):
        return []

    # Method to get daily event counts for a given employee or team
    def event_counts(self, id):
        id_column = f"{self.name}_id"
        query = f"""
            SELECT event_date,
                   SUM(positive_events) AS positive_events,
                   SUM(negative_events) AS negative_events
            FROM employee_events
            WHERE {id_column} = {id}
            GROUP BY event_date
            ORDER BY event_date
        """
        return QueryMixin().pandas_query(query)

    # Method to get notes for a given employee or team
    def notes(self, id):
        id_column = f"{self.name}_id"
        query = f"""
            SELECT note_date, note
            FROM notes
            WHERE {id_column} = {id}
            ORDER BY note_date
        """
        return QueryMixin().pandas_query(query)
