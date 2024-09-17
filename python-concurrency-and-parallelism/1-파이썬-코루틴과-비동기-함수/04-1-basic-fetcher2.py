import requests
import aiohttp
import time
import asyncio

async def fetcher(session, url):
    # url에 해당하는 데이터 반환
    # await : 비동기로 처리, return을 위해 async로 선언
    async with session.get(url) as response:
        return await response.text()


async def main():
    # Blocking 발생
    # 10초 정도 걸림
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"]
    # 세션을 열었다가, 바로 자동으로 닫기 위해서
    async with aiohttp.ClientSession() as session:
        # result = [fetcher(session, url) for url in urls]
        # print(result) 
        # 모든 데이터 반환
        
        result = await fetcher(session, urls[0])
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
