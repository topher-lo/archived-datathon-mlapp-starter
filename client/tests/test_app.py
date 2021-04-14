"""Unit tests for running and querying Prefect flow runs from the Streamlit app.
"""

import pytest

from client.app import create_prefect_flow_run


@pytest.mark.apitest
def test_create_prefect_flow_run():
    flow_name = 'mock_flow'
    project_name = 'streamlit-e2e-boilerplate'
    task_refs = ['merged_token_counts']

    url = ('https://raw.githubusercontent.com/KTH/ci-hackathon/master/'
           'installations/ci-poetry/supercollider_src/poet10/poem.txt')
    params = {'url': url}
    result, state, task_res_locs = create_prefect_flow_run(
        flow_name,
        project_name,
        task_refs,
        params
    )
    # Get top 3 tokens
    result_top_tokens = sorted(result, key=lambda x: x[1])[:3]
    expected_top_tokens = [('a', 4), ('and', 4), ('an', 1)]
    assert result_top_tokens == expected_top_tokens


if __name__ == "__main__":
    pass
