import httpx
from httpx import AsyncClient
from starlette.status import HTTP_200_OK

from app import app
from app.utils.edge import edgedb_client


async def test_api_create_meeting_edgedb() -> None:
    # Given: 원래는 테스트에 필요한 데이터를 준비하는 과정
    # meeting 생성에는 특별히 인자가 필요없기 때문에 생략

    # When
    async with AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post(
            url="/v1/edgedb/meetings",
        )

    # Then: 테스트 결과 검증
    # http는 문자열을 주고 받는 프로토콜
    # 응답으로 온 데이터가 json이 아닐 수 있음

    # 주로 언제 json이 아닌 응답이 오는가?
    # nginx의 default 500 응답 -> html
    # 즉, 진짜 문제가 숨겨진다!!!!
    assert response.status_code == HTTP_200_OK
    url_code = response.json()["url_code"]
    assert await edgedb_client.query_single(f"select exists (select Meeting filter .url_code = '{url_code}');") is True
    # response.json()
