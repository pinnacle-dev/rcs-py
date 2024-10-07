# Reference
<details><summary><code>client.<a href="src/rcs/client.py">check_rcs_capability</a>(...)</code></summary>
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
from rcs import Pinnacle

client = Pinnacle(
    api_key="YOUR_API_KEY",
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

**phone_number:** `PhoneNumber` — Phone number (E.164 format: [+][country code][subscriber number including area code]) to check for RCS capability. Example: +1234567890
    
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

<details><summary><code>client.<a href="src/rcs/client.py">update_settings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initializes settings related to RCS messaging, including webhook registration.
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
client.update_settings(
    webhook_url="webhook_url",
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

**webhook_url:** `str` — Webhook URL to receive inbound messages
    
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

<details><summary><code>client.<a href="src/rcs/client.py">get_account_number</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the phone number associated with the account.
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
client.get_account_number()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/rcs/client.py">send_message</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a SMS or RCS message to a phone number
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
from rcs import Card, CardRcs, CardRcsMessage, Pinnacle

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.send_message(
    request=CardRcs(
        phone_number="phone_number",
        message=CardRcsMessage(
            cards=[
                Card(
                    title="title",
                )
            ],
        ),
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

**request:** `SendMessageRequest` 
    
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

