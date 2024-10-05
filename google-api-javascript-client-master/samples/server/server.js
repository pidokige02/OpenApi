// server.js
const express = require('express');
const cors = require('cors');
const { SecretManagerServiceClient } = require('@google-cloud/secret-manager');

const app = express();
const port = 3001; // 서버 포트 설정
const client = new SecretManagerServiceClient();

app.use(cors());
app.use(express.json());

// 비밀 관리에서 클라이언트 ID와 API 키를 가져오는 함수
async function getSecrets() {
    const [apiKeyVersion] = await client.accessSecretVersion({
        name: 'projects/symmetric-curve-436423-i6/secrets/api_key_secret/versions/latest',
    });

    const [clientIdVersion] = await client.accessSecretVersion({
        name: 'projects/symmetric-curve-436423-i6/secrets/clientId_secret/versions/latest',
    });

    return {
        apiKey: apiKeyVersion.payload.data.toString('utf8'),
        clientId: clientIdVersion.payload.data.toString('utf8'),
    };
}

// 클라이언트 요청을 처리하는 엔드포인트
app.get('/api/secrets', async (req, res) => {
    try {
        const secrets = await getSecrets();
        res.json(secrets);
    } catch (error) {
        console.error('Error accessing secret:', error);
        res.status(500).send('서버 오류');
    }
});

app.listen(port, () => {
    console.log(`서버가 http://localhost:${port}에서 실행 중입니다.`);
});
