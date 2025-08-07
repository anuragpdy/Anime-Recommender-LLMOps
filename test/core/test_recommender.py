import pytest
from unittest.mock import MagicMock
from core.recommender import AnimeRecommender

# This is a placeholder test file to demonstrate structure.
# In a real project, these tests would be fully implemented.

def test_recommender_initialization():
    """
    Tests if the AnimeRecommender class initializes correctly without errors.
    We use a "MagicMock" to simulate the retriever object, so we don't
    need a real database for this test.
    """
    # ARRANGE: Create a fake retriever object
    mock_retriever = MagicMock()

    # ACT: Initialize the recommender
    try:
        recommender = AnimeRecommender(
            retriever=mock_retriever,
            api_key="fake_api_key",
            model_name="fake_model"
        )
        # ASSERT: Check if the object was created
        assert recommender is not None
        assert recommender.qa_chain is not None
    except Exception as e:
        pytest.fail(f"AnimeRecommender initialization failed with an exception: {e}")


def test_get_recommendation_calls_chain():
    """
    Tests if the get_recommendation method correctly calls the internal QA chain.
    """
    # ARRANGE: Create a fake retriever and a recommender instance
    mock_retriever = MagicMock()
    recommender = AnimeRecommender(
        retriever=mock_retriever,
        api_key="fake_api_key",
        model_name="fake_model"
    )

    # Mock the internal chain to track if it's called
    recommender.qa_chain = MagicMock(return_value={'result': 'a_test_recommendation'})

    # ACT: Call the method we are testing
    query = "test query"
    result = recommender.get_recommendation(query)

    # ASSERT: Check that the internal chain was called once with the correct query
    recommender.qa_chain.assert_called_once_with({"query": query})
    # ASSERT: Check that the result is what we expect
    assert result == 'a_test_recommendation'