```bash
(venv-py39) [repairman@vmhub az-unittest-toolboxs]$ pytest -v test-aoai.py 
================================================================================= test session starts =================================================================================
platform linux -- Python 3.9.18, pytest-7.4.3, pluggy-1.3.0 -- /home/repairman/az-unittest-toolboxs/venv-py39/bin/python3
cachedir: .pytest_cache
rootdir: /home/repairman/az-unittest-toolboxs
configfile: pytest.ini
plugins: anyio-3.7.1, testinfra-10.0.0
collected 4 items                                                                                                                                                                     

test-aoai.py::TestAzureOpenAIEndpoints::test_prompt PASSED                                                                                                                      [ 25%]
test-aoai.py::TestAzureOpenAIEndpoints::test_to_aoai_endpoint_dns PASSED                                                                                                        [ 50%]
test-aoai.py::TestAzureOpenAIEndpoints::test_to_aoai_endpoint_https PASSED                                                                                                      [ 75%]
test-aoai.py::TestAzureOpenAIEndpoints::test_to_aoai_endpoint_ip PASSED                                                                                                         [100%]

================================================================================= 4 passed in 18.98s ==================================================================================
```
