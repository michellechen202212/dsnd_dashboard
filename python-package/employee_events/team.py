# Import the QueryBase class
from employee_events.query_base import QueryBase

# Import dependencies for sql execution
from employee_events.sql_execution import QueryMixin

# Create a subclass of QueryBase
# called `Team`
class Team(QueryBase):

    # Set the class attribute `name`
    # to the string "team"
    name = "team"

    # Define a `names` method
    # that receives no arguments
    # This method should return
    # a list of tuples from an sql execution
    def names(self):
        # Query 5
        query = f"""
            SELECT team_name, team_id
            FROM {self.name}
        """
        return QueryMixin().query(query)

    # Define a `username` method
    # that receives an ID argument
    # This method should return
    # a list of tuples from an sql execution
    def username(self, id):
        # Query 6
        query = f"""
            SELECT team_name
            FROM {self.name}
            WHERE {self.name}_id = {id}
        """
        return QueryMixin().query(query)
    
    def details(self, id):
        # Query 7
        # get team details from team table
        # team_id, team_name, shift, manager_name
        # no need to join with employee table
        query = f"""
            SELECT {self.name}.*
            FROM {self.name}
            WHERE {self.name}.{self.name}_id = {id}
        """
        return QueryMixin().query(query)

            
    
    def employees(self, id):
        # Query to select all employees in the team with the given team_id
        query = f"""
            SELECT e.employee_id,
                e.first_name || ' ' || e.last_name AS full_name
            FROM employee e
            JOIN team t ON e.team_id = t.team_id
            WHERE t.team_id = {id}
        """
        return QueryMixin().query(query)


    # Method that returns a pandas dataframe for model data
    def model_data(self, id):
        query = f"""
            SELECT positive_events, negative_events FROM (
                SELECT employee_id,
                       SUM(positive_events) AS positive_events,
                       SUM(negative_events) AS negative_events
                FROM {self.name}
                JOIN employee_events
                    USING({self.name}_id)
                WHERE {self.name}.{self.name}_id = {id}
                GROUP BY employee_id
            )
        """
        return QueryMixin().pandas_query(query)
