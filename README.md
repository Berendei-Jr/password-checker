# Password checker
## Клиент-серверное приложение для безопасной проверки проверки связки логин/пароль на наличие в базах скомпрометированных данных.

### Принцип работы:
1) Когда клиент вводит пару логин/пароль, клиентское приложение вычисляет хеш sha256 пароля и передает данные на сервер в виде [логин, хеш пароля]. Хеш передается не целиком, а возможны варианты 25, 50 и 100% длины хеша. Если текущая точность не устраивает пользователя, он может ее увеличить, либо остановиться.
2) Сервер может позволить себе хранить пароли в открытом виде, так как они все равно скомпрометированы, но это не обязательно. Для оптимальной работы на сервере хранятся хеши паролей, поэтому, при получении запроса клиента, происходит поиск заданного хеша в базе. Если совпадения не нашлось, значит, пароль не скомпрометирован, а сервер не узнал, какой пароль ввел пользователь (можно конечно попробовать сбрутить его, но это занятие неблагодарное при достаточной сложности пароля).
3) Сервер работает с той частью хеша, который прислал клиент. Если сервер нашел совпадение, сервер сообщает клиенту, что пароль возможно присутсвует в базе, необходимо увеличить точность. В противном случае сервер сообщает клиенту, что введенные данные безопасны. Если было найдено точное совпадение пары логин/пароль при точности 100% - пользователь получает соответствующее сообщение, иначе просто будет сообщение о том, что такой пароль найден в базе.

### API:
Сервис принимает POST запрос по адресу http://<server_url>:8000/api/v1/password_check в формате JSON:  
> { 'login': str, 'password_hash': str' }

Если хеш неполный - ничего страшного, поиск будет произведен по переданной части. Поле логин необязательное.
Ответ сервера придет также в виде JSON:
> { 'result': int }

Код возврата 0 означает, что пара логин/пароль в базе не найдена.  
Код 1 - найден пароль с каким-то другим логином.  
Код 2 - найден пароль в паре с заданным логином.

### Безопасная пара логин/пароль:
![Full size](https://github.com/Berendei-Jr/password_checker/blob/main/images/secure_credentials.png)

### Скомпрометированный пароль:
![Full size](https://github.com/Berendei-Jr/password_checker/blob/main/images/pass_compromised.png)

### Скомпрометированная пара логин/пароль:
![Full size](https://github.com/Berendei-Jr/password_checker/blob/main/images/pair_compromised.png)
