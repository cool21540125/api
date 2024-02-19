
# 使用 OAuth 取得 access token

- 參考
    - https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/
    - https://www.youtube.com/watch?v=rb_SZE6Sh20
        - 這篇的教學採用的是 Authorization code grant
- Bitbucket Account - API Tokens
    - https://id.atlassian.com/manage-profile/security/api-tokens
- process
    - 進入 https://bitbucket.org/cool21540125/workspace/settings/api
        - 建立一個 OAuth consumers
            - Callback URL 隨便打, 就用 https://github.com 吧
            - 底下的 Permissions 自行勾選
        - 建立完成後, 點開剛剛建立的 OAuth consumer
            - Key 即為 client_id (username)
            - Secret 即為 client_secret (password)
    - 訪問 https://bitbucket.org/site/oauth2/authorize?client_id={{client_id}}&response_type=code
        - 訪問後會 redirect 到上面填寫的 Callback URL, 網址最後可拿到 code, 例如: gtPq8calC3ujRv8BxH
    - 然後尻底下的 API

```http
POST https://bitbucket.org/site/oauth2/access_token
Content-Type: application/x-www-form-urlencoded
Authorization: Basic {{username}} {{password}}

grant_type=authorization_code
&code={{code}}
```

拿到了這一包

```json
{
  "access_token": "gK-I4IcAwfG1EQxlgp4zohkNTrQvUK51LcJLipDm1IBZr1UjvI1q9I562dkLFfu7tLkSfJ5OprgQ3t5t2l3ONodq7vadzEmJFg-P1cuA1R6abDlhwvHUm0qI1yaLtVzdD8xSPtfmlmem4tg5sfITviZMKXj",
  "scopes": "project:read project:admin webhook",
  "token_type": "bearer",
  "expires_in": 7200,
  "state": "authorization_code",
  "refresh_token": "jnMxzuHoCjZfXmFhDd"
}
```

上面拿到的 access_token 便是 token
