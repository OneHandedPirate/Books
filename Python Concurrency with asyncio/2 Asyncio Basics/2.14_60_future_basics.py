from asyncio import Future


my_future = Future()

print(f'Is my_future done? {my_future.done()}')

my_future.set_result(52)

print(f'Is my_future done? {my_future.done()}')

print(f'Get result from my_future {my_future.result()}')



