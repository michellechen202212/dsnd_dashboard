# Import the QueryBase class
from employee_events.query_base import QueryBase

# Import dependencies needed for sql execution
# from the `sql_execution` module
from employee_events.sql_execution import QueryMixin

# Define a subclass of QueryBase
# called Employee
class Employee(QueryBase):

    # Set the class attribute `name`
    # to the string "employee"
    name = "employee"

    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution
    def names(self):
        # Query 3
        # SQL query to select full name and id of all employees
        query = f"""
            SELECT first_name || ' ' || last_name AS full_name, {self.name}_id
            FROM {self.name}
        """
        return QueryMixin().query(query)

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    def username(self, id):
        # Query 4
        # SQL query to select full name of employee with given id
        query = f"""
            SELECT first_name || ' ' || last_name AS full_name,
            FROM {self.name}
            WHERE {self.name}_id = {id}
        """
        return QueryMixin().query(query)
    
    def details(self, id):
        # Query 5
        # SQL query to select all details of an employee with given id
        # get details of employee from team table as well
        query = f"""
            SELECT {self.name}.*,
                   team.team_name,
                   team.shift,
                   team.manager_name
            FROM {self.name}
            JOIN team
                USING(team_id)
            WHERE {self.name}.{self.name}_id = {id}
        """
        return QueryMixin().query(query)

    # Method that returns a pandas dataframe for model data
    def model_data(self, id):
        query = f"""
            SELECT SUM(positive_events) positive_events,
                   SUM(negative_events) negative_events
            FROM {self.name}
            JOIN employee_events
                USING({self.name}_id)
            WHERE {self.name}.{self.name}_id = {id}
        """
        return QueryMixin().pandas_query(query)
