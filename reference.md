# Reference
<details><summary><code>client.<a href="src/rcs/base_client.py">get_rcs_functionality</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the RCS functionality of a phone number. For example checks if a phone number can receive RCS message and if it can receive RCS carousels.
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
from rcs import Pinnacle

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.get_rcs_functionality()

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

**phone_number:** `typing.Optional[str]` — The phone number to check for RCS functionality. Should be in E.164 format (i.e. +12345678901).
    
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

## Company
<details><summary><code>client.company.<a href="src/rcs/company/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the company's information (i.e. approval status, company name, etc.). Search by company ID or company name.
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
from rcs import Pinnacle

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.company.get()

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

**company_id:** `typing.Optional[int]` — The unique identifier for the company
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[str]` — The name of the company
    
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

<details><summary><code>client.company.<a href="src/rcs/company/client.py">register</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register a company for RCS with the Pinnacle platform
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
from rcs import Pinnacle
from rcs.company import CompanyRegisterRequestCompanyId

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.company.register(
    request=CompanyRegisterRequestCompanyId(
        company_id="companyId",
    ),
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

**request:** `CompanyRegisterRequest` 
    
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

<details><summary><code>client.company.<a href="src/rcs/company/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upsert a company on the Pinnacle platform
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
from rcs import Pinnacle

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.company.update()

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

**company_id:** `typing.Optional[str]` — Optional company ID. If provided, updates existing company. If not provided, creates a new company.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[Company]` 
    
</dd>
</dl>

<dl>
<dd>

**company_contact:** `typing.Optional[CompanyContact]` 
    
</dd>
</dl>

<dl>
<dd>

**messaging:** `typing.Optional[Messaging]` 
    
</dd>
</dl>

<dl>
<dd>

**point_of_contact:** `typing.Optional[PointOfContact]` 
    
</dd>
</dl>

<dl>
<dd>

**optionals:** `typing.Optional[Optionals]` 
    
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

## Send
<details><summary><code>client.send.<a href="src/rcs/send/client.py">rcs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send an interactive RCS message with text, media, or cards. Each message can only contain either text, media, or card(s).

Quick replies can also be added to the message.
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
from rcs import Pinnacle

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.send.rcs(
    from_="from",
    to="to",
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

**from_:** `str` 

The id of the RCS agent sending the message.

Use 'test' if you want to send from the Pinnacle test agent. The test agent can only send to whitelisted test numbers.

See https://dashboard.trypinnacle.app/settings/test-numbers to whitelist a number.
    
</dd>
</dl>

<dl>
<dd>

**to:** `str` — The recipient's RCS-enabled phone number in E.164 format (e.g., +12345678901).
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` 

Text content of the message.

Make sure you have either 'text', 'mediaUrl', or 'cards'. An error will be thrown if multiple (i.e. both 'text' and 'mediaUrl') is provided.
    
</dd>
</dl>

<dl>
<dd>

**media_url:** `typing.Optional[str]` 

Media URL to be included in the message.

Make sure you have either 'text', 'mediaUrl', or 'cards'. An error will be thrown if multiple (i.e. both 'text' and 'mediaUrl') is provided.
    
</dd>
</dl>

<dl>
<dd>

**cards:** `typing.Optional[typing.Sequence[Card]]` 

List of rich cards. Maximum of 10 cards. 

Make sure you have either 'text', 'mediaUrl', or 'cards'. An error will be thrown if multiple (i.e. both 'text' and 'mediaUrl') is provided.
    
</dd>
</dl>

<dl>
<dd>

**quick_replies:** `typing.Optional[typing.Sequence[Action]]` — Optional list of quick reply actions (max 10).
    
</dd>
</dl>

<dl>
<dd>

**fallback:** `typing.Optional[RcsFallback]` 
    
</dd>
</dl>

<dl>
<dd>

**status_callback:** `typing.Optional[str]` — Optional URL to receive a POST request when the message status changes. Read more about status callbacks [here](/api-reference/receive-msg-statuses).
    
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

<details><summary><code>client.send.<a href="src/rcs/send/client.py">sms</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send an SMS message to a recipient.
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
from rcs import Pinnacle

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.send.sms(
    to="to",
    from_="from",
    text="text",
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

**to:** `str` — The recipient's phone number in E.164 format (e.g., +12345678901).
    
</dd>
</dl>

<dl>
<dd>

**from_:** `str` — The sender's phone number in E.164 format. Must be owned by the user.
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — The SMS message content (max 1600 characters).
    
</dd>
</dl>

<dl>
<dd>

**status_callback:** `typing.Optional[str]` — Optional URL to receive a POST request when the message status changes. Read more about status callbacks [here](/api-reference/receive-msg-statuses).
    
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

<details><summary><code>client.send.<a href="src/rcs/send/client.py">mms</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send an MMS message with media attachments.
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
from rcs import Pinnacle

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.send.mms(
    to="to",
    from_="from",
    media_urls=[
        "https://example.com/image1.jpg",
        "https://example.com/video.mp4",
    ],
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

**to:** `str` — The recipient's phone number in E.164 format (e.g., +12345678901).
    
</dd>
</dl>

<dl>
<dd>

**from_:** `str` — The sender's phone number in E.164 format. Must be owned by the user.
    
</dd>
</dl>

<dl>
<dd>

**media_urls:** `typing.Sequence[str]` — The URLs of media to include. `jpeg`, `jpg`, `gif`, and `png` file types are fully supported and have a size limit of 5 MB. 500 KB limit for other types. Up to 10 media URLs can be included.
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` — The MMS message content (max 1600 characters).
    
</dd>
</dl>

<dl>
<dd>

**status_callback:** `typing.Optional[str]` — Optional URL to receive a POST request when the message status changes. Read more about status callbacks [here](/api-reference/receive-msg-statuses).
    
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

## Tools
<details><summary><code>client.tools.<a href="src/rcs/tools/client.py">shorten_url</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a shortened URL with an optional expiration date (default and max expiration is 90 days). The shortened URL will redirect to the original URL and will have the following format https://urls.p1n.io/ABCD5678.
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
from rcs import Pinnacle

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.tools.shorten_url(
    url="https://example.com",
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

**url:** `str` — The URL to be shortened. Must be a valid URL with either http or https protocol.
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[dt.datetime]` — Optional expiration date for the shortened URL in ISO 8601 format. Default and max expiration is 90 days.
    
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

<details><summary><code>client.tools.<a href="src/rcs/tools/client.py">upload_url</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate signed upload (expires in 2 hours) and download URLs for a file (expires in 1 hour).

See the [Upload](/api-reference/upload) page for native Python and Typescript SDKs.
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
from rcs import Pinnacle

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.tools.upload_url(
    content_type="image/png",
    size=1024,
    name="example.png",
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

**content_type:** `str` 

The MIME type of the file. 

Supported types are audio/basic, audio/L24, audio/mp4, audio/mpeg, audio/mpg, audio/mp3, audio/ogg, audio/aac, audio/vndrn-realaudio, audio/vndwave, audio/3gpp, audio/3gpp2, audio/ac3, audio/webm, audio/amrnb, audio/amr, video/mpeg, video/mp4, video/quicktime, video/webm, video/3gpp, video/3gpp2, video/3gpptt, video/H261, video/H263, video/H2631998, video/H2632000, video/H264, video/m4v, video/mpeg4, video/webm, image/jpeg, image/gif, image/png, image/gif, image/bmp, image/tiff, image/webp, text/vcard, text/xvcard, text/csv, text/rtf, text/richtext, text/calendar, text/directory, application/ogg, application/pdf, application/vcard, application/vndapple.pkpass.
    
</dd>
</dl>

<dl>
<dd>

**size:** `int` — The size of the file in bytes. Should be less than 100 MB.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the file.
    
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

