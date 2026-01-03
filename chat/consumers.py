# chat/consumers.py
import aiohttp# type: ignore
import json
from channels.generic.websocket import AsyncWebsocketConsumer # type: ignore

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, _):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        prompt = data['prompt']
        model = data.get('model', 'deepseek-r1:1.5b')

        async with aiohttp.ClientSession() as session:
            async with session.post(
                "http://localhost:11434/api/generate",
                json={"model": model, "prompt": prompt, "stream": True}
            ) as resp:
                async for line in resp.content:
                    if not line:
                        continue
                    try:
                        content = json.loads(line.decode())
                        await self.send(json.dumps({'response': content.get('response', '')}))
                    except:
                        pass