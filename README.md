# mock
Learning how to use mock

source https://realpython.com/blog/python/testing-third-party-apis-with-mocks/

**When to use coding methods:**

1. Use a decorator when all of the code in your test function body uses a mock.
2. Use a context manager when some of the code in your test function uses a mock and other code references the actual function.
3. Use a patcher when you need to explicitly start and stop mocking a function across multiple tests (e.g. the setUp() and tearDown() functions in a test class).