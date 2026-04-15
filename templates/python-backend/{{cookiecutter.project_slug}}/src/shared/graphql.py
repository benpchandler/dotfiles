"""GraphQL configuration and setup."""
from typing import Optional

import strawberry
from strawberry.fastapi import GraphQLRouter

from src.shared.config import settings


@strawberry.type
class Query:
    """Root GraphQL query type."""
    
    @strawberry.field
    def hello(self, name: Optional[str] = None) -> str:
        """Example query field."""
        return f"Hello, {name or 'World'}!"


@strawberry.type
class Mutation:
    """Root GraphQL mutation type."""
    
    @strawberry.mutation
    def echo(self, message: str) -> str:
        """Example mutation."""
        return message


# Create the GraphQL schema
schema = strawberry.Schema(query=Query, mutation=Mutation)

# Create the GraphQL app
graphql_app = GraphQLRouter(
    schema,
    path="/",
    graphiql=settings.DEBUG,  # Enable GraphiQL in debug mode
)


# To add feature-specific types and resolvers:
# 1. Import types from your features
# 2. Use strawberry.federation or merge schemas
# 3. Or extend the Query/Mutation classes

"""
Example of adding feature types:

from src.features.todo.graphql import TodoQuery, TodoMutation

@strawberry.type
class Query(TodoQuery):
    pass

@strawberry.type  
class Mutation(TodoMutation):
    pass
"""