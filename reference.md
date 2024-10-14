# Reference
<details><summary><code>client.<a href="src/rcs/client.py">get_rcs_functionality</a>(...)</code></summary>
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

<details><summary><code>client.<a href="src/rcs/client.py">get_company</a>(...)</code></summary>
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
client.get_company()

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

<details><summary><code>client.<a href="src/rcs/client.py">register_company</a>(...)</code></summary>
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
from rcs import CompanyContact, CompanyDetails, Pinnacle, PointOfContact

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.register_company(
    company=CompanyDetails(
        name="name",
        address="address",
        ein="ein",
        description="description",
        brand_color="brandColor",
        logo_url="logoUrl",
        hero_url="heroUrl",
    ),
    company_contact=CompanyContact(
        primary_website_url="primaryWebsiteUrl",
        primary_website_label="primaryWebsiteLabel",
        primary_phone="primaryPhone",
        primary_phone_label="primaryPhoneLabel",
        primary_email="primaryEmail",
        primary_email_label="primaryEmailLabel",
        privacy_policy_url="privacyPolicyUrl",
        tos_url="tosUrl",
    ),
    point_of_contact=PointOfContact(
        poc_name="pocName",
        poc_title="pocTitle",
        poc_email="pocEmail",
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

**company:** `CompanyDetails` 
    
</dd>
</dl>

<dl>
<dd>

**company_contact:** `CompanyContact` 
    
</dd>
</dl>

<dl>
<dd>

**point_of_contact:** `PointOfContact` 
    
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

<details><summary><code>client.<a href="src/rcs/client.py">update_company</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a company on the Pinnacle platform
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
client.update_company(
    company_id="companyId",
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

**company_id:** `str` 
    
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
    text="text",
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

**text:** `str` — The MMS message content (max 1600 characters).
    
</dd>
</dl>

<dl>
<dd>

**media_urls:** `typing.Sequence[str]` — The URLs of media to include. `jpeg`, `jpg`, `gif`, and `png` file types are fully supported and have a size limit of 5 MB. 500 KB limit for other types. Up to 10 media URLs can be included.
    
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

