# Reference
<details><summary><code>client.<a href="src/pinnacle/client.py">check_rcs_capability</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Checks if a phone number is able to receive RCS
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pinnacle import Pinnacle

client = Pinnacle(
    pinnacle_api_key="YOUR_PINNACLE_API_KEY",
)
client.check_rcs_capability(
    phone_number="phone_number",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**phone_number:** `str` — The phone number to check for RCS capability
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/pinnacle/client.py">receive_rcs_messages</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pinnacle import Pinnacle

client = Pinnacle(
    pinnacle_api_key="YOUR_PINNACLE_API_KEY",
)
client.receive_rcs_messages()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — Webhook URL to receive RCS messages
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/pinnacle/client.py">send_an_rcs_message</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pinnacle import Pinnacle, RcsMessage

client = Pinnacle(
    pinnacle_api_key="YOUR_PINNACLE_API_KEY",
)
client.send_an_rcs_message(
    request=RcsMessage(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `SendAnRcsMessageRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

