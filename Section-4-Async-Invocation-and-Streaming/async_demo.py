
# ASYNC CAN'T RUN IN JUPYTER NOTEBOOK
"""
1. Ưu điểm của ASYNC (bất đồng bộ):
- Tối ưu hiệu suất:
Khi các node cần chờ đợi thao tác lâu (gọi API, database, đọc/ghi file…), async cho phép các tác vụ khác vẫn tiếp tục chạy thay vì bị “đứng” chờ.
- Giảm thời gian chờ tổng thể:
Khi có nhiều tác vụ I/O, async giúp xử lý song song nhiều tác vụ, tiết kiệm thời gian tổng thể.
- Không block thread chính:
Trong các ứng dụng cần xử lý đồng thời nhiều yêu cầu (ví dụ web service, workflow lớn), async giúp ứng dụng không bị block, tăng khả năng đáp ứng.

2. Ví dụ thực tế cần ASYNC:
- Các node truy vấn nhiều API bên ngoài (ví dụ LLM, search engine, crawler…).
- Đọc/ghi nhiều file dữ liệu lớn cùng lúc.
- Chạy trên server phục vụ nhiều user, mỗi user là một workflow riêng biệt.

3. Khi nào KHÔNG cần dùng ASYNC:
- Khi mọi thao tác của bạn đều là tính toán ngắn, không có thao tác I/O, không cần chạy song song.
- Khi bạn muốn code đơn giản, dễ debug, dễ chạy thử.

"""

from typing import TypedDict
from langgraph.graph import END, START, StateGraph
import asyncio


class HelloWorldState(TypedDict):
    message: str


async def hello(state: HelloWorldState):
    print(f"Hello Node: {state['message']}")
    # TODO: Simulate Async Processing
    await asyncio.sleep(5)
    return {"message": "Hello " + state['message']}


async def bye(state: HelloWorldState):
    print(f"Bye Node: {state['message']}")
    # TODO: Simulate Async Processing
    await asyncio.sleep(5)
    return {"message": "Bye " + state['message']}


graph = StateGraph(HelloWorldState)
graph.add_node("hello", hello)
graph.add_node("bye", bye)

graph.add_edge(START, "hello")
graph.add_edge("hello", "bye")
graph.add_edge("bye", END)

runnable = graph.compile()


# TODO: Async Invocation
async def main():
    output = await runnable.ainvoke({"message": "Lam Nguyen"})
    print(output)

asyncio.run(main())
