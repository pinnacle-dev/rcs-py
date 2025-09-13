# Reference
## Brands
<details><summary><code>client.brands.<a href="src/rcs/brands/client.py">autofill</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Automatically populate brand information based on partial input data you provide.
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
from rcs.brands import AutofillBrandSchemaOptions

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.brands.autofill(
    additional_info="A developer-friendly, compliant API for SMS, MMS, and RCS, built to scale real conversations.",
    name="Pinnacle",
    options=AutofillBrandSchemaOptions(
        force_reload=True,
    ),
    website="https://www.pinnacle.sh",
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

**additional_info:** `typing.Optional[str]` — Any extra details about the brand to help improve data accuracy.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the brand.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[AutofillBrandSchemaOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — Brand's website URL.
    
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

<details><summary><code>client.brands.<a href="src/rcs/brands/client.py">upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new brand or update an existing brand by with the provided information.
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
from rcs import NullableContact, Pinnacle

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.brands.upsert(
    address="500 Folsom St, San Francisco, CA 94105",
    contact=NullableContact(
        email="michael.chen@trypinnacle.app",
        name="Michael Chen",
        phone="+14155551234",
        title="Customer Support Representative",
    ),
    dba="Pinnacle RCS",
    description="A developer-friendly, compliant API for SMS, MMS, and RCS, built to scale real conversations.",
    ein="88-1234567",
    email="founders@trypinnacle.app",
    id=1,
    name="Pinnacle",
    sector="TECHNOLOGY",
    type="PRIVATE_PROFIT",
    website="https://www.pinnacle.sh",
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

**address:** `typing.Optional[str]` — Primary brand address where the company is located.
    
</dd>
</dl>

<dl>
<dd>

**contact:** `typing.Optional[NullableContact]` — Contact information for the brand.
    
</dd>
</dl>

<dl>
<dd>

**dba:** `typing.Optional[str]` — "Doing Business As" name - the public name the brand operates under.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Brief description of what the brand does.
    
</dd>
</dl>

<dl>
<dd>

**ein:** `typing.Optional[str]` — Brand's Employer Identification Number (EIN) assigned by the IRS.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Main contact email address for the brand.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` — Brand ID - include only when updating an existing brand, omit to create a new one.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Legal name of the brand as registered.
    
</dd>
</dl>

<dl>
<dd>

**sector:** `typing.Optional[CompanySectorEnum]` — Industry the brand operates in.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[CompanyTypeEnum]` — Legal structure of the brand.
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — Brand website URL.
    
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

<details><summary><code>client.brands.<a href="src/rcs/brands/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve detailed information for a specific brand in your account by ID.
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
client.brands.get(
    id=1,
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

**id:** `int` — ID of an existing brand in your account that you want to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**hide_ein:** `typing.Optional[bool]` 

Optional flag to mask the Employer Identification Number in the response for security purposes.<br>

When you set this to true, the EIN value will be replaced with a masked placeholder instead of the actual number.
    
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

<details><summary><code>client.brands.<a href="src/rcs/brands/client.py">submit</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit your brand for review and approval by the compliance team.
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
client.brands.submit(
    brand_id=1,
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

**brand_id:** `int` 

The unique identifier of the brand you want to submit for review. <br>

Must correspond to an existing brand in your account that is ready for submission.
    
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

<details><summary><code>client.brands.<a href="src/rcs/brands/client.py">validate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validate your brand information for compliance and correctness before submission or storage.
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
from rcs.brands import BrandContact

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.brands.validate(
    address="500 Folsom St, San Francisco, CA 94105",
    contact=BrandContact(
        email="michael.chen@trypinnacle.app",
        name="Michael Chen",
        phone="+14155551234",
        title="Customer Support Representative",
    ),
    dba="Pinnacle Messaging",
    description="Pinnacle is an SMS, MMS, and RCS API for scaling conversations with customers you value.",
    ein="88-1234567",
    email="founders@trypinnacle.app",
    name="Pinnacle",
    sector="TECHNOLOGY",
    type="PRIVATE_PROFIT",
    website="https://www.pinnacle.sh",
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

**address:** `str` — Primary brand address where the brand is located.
    
</dd>
</dl>

<dl>
<dd>

**contact:** `BrandContact` — Contact information for the primary brand representative.
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — Brief description of what the brand does.
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Main contact email address for the brand.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Legal name of the brand as registered.
    
</dd>
</dl>

<dl>
<dd>

**sector:** `CompanySectorEnum` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `CompanyTypeEnum` 
    
</dd>
</dl>

<dl>
<dd>

**website:** `str` — Brand website URL.
    
</dd>
</dl>

<dl>
<dd>

**dba:** `typing.Optional[str]` — "Doing Business As" name - the public name the brand operates under.
    
</dd>
</dl>

<dl>
<dd>

**ein:** `typing.Optional[str]` — Employer Identification Number (EIN) assigned by the IRS.
    
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

<details><summary><code>client.brands.<a href="src/rcs/brands/client.py">vet</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit a brand for external vetting verification to enhance your brand's trust score and improved message delivery rates.
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
client.brands.vet(
    brand_id=1,
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

**brand_id:** `int` 

The unique identifier of the brand to vet. <br>

The brand must be already registered before it can be vetted.
    
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

## Contacts
<details><summary><code>client.contacts.<a href="src/rcs/contacts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve contact information for a given number.
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
client.contacts.get()

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

**id:** `typing.Optional[int]` 

Unique identifier of a specific contact you want to retrieve. <br>

Either this parameter or `phoneNumber` must be provided, but not both.
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — Phone number you want to look up contact information for, provided in URL-encoded E.164 format with %2B prefix instead of +.
    
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

<details><summary><code>client.contacts.<a href="src/rcs/contacts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new contact for a given phone number.
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
client.contacts.create(
    phone_number="phoneNumber",
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

**phone_number:** `str` — Phone number to save for your contact, in E.164 format.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — New notes or details for your contact.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — New email address for your contact.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — New name for your contact.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — New tags for your contact.
    
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

<details><summary><code>client.contacts.<a href="src/rcs/contacts/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing contact.
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
client.contacts.update(
    description="Retired",
    email="alvaroopedtech@pinnacle.sh",
    name="Retired Bestie",
    tags=["friend"],
    id=137,
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

**id:** `int` — ID of the contact you want to update.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — New notes or details for your contact.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — New email address for your contact.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — New name for your contact.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — New tags for your contact.
    
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

## Conversations
<details><summary><code>client.conversations.<a href="src/rcs/conversations/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch a specific conversation using either its unique identifier or by matching sender and recipient details.
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
from rcs import GetConversationRequestId, Pinnacle

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.conversations.get(
    request=GetConversationRequestId(
        id=1,
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

**request:** `GetConversationParams` 
    
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

<details><summary><code>client.conversations.<a href="src/rcs/conversations/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves conversations by page with optional filtering based off provided parameters.
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
client.conversations.list(
    brand_id=101,
    campaign_id=136,
    campaign_type="TOLL_FREE",
    page_index=0,
    page_size=20,
    receiver="+16509231662",
    sender="+18445551234",
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

**page_index:** `int` — Zero-based index for pagination.
    
</dd>
</dl>

<dl>
<dd>

**brand_id:** `typing.Optional[int]` — The unique identifier of the brand to filter conversations.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[int]` — The unique identifier of the campaign to filter conversations.
    
</dd>
</dl>

<dl>
<dd>

**campaign_type:** `typing.Optional[CampaignEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of conversations to return per page.
    
</dd>
</dl>

<dl>
<dd>

**receiver:** `typing.Optional[str]` — Receiver's phone number in E.164 format.
    
</dd>
</dl>

<dl>
<dd>

**sender:** `typing.Optional[Sender]` 
    
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

<details><summary><code>client.conversations.<a href="src/rcs/conversations/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the notes associated with a specific conversation.
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
client.conversations.update(
    id=123,
    notes="Follow-up completed. Customer satisfied with resolution.",
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

**id:** `int` — The unique identifier of the conversation to update.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `str` — New notes or comments for the conversation.
    
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

## Messages
<details><summary><code>client.messages.<a href="src/rcs/messages/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a previously sent message.
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
client.messages.get(
    id=1240,
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

**id:** `int` — Unique identifier of the message.
    
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

<details><summary><code>client.messages.<a href="src/rcs/messages/client.py">react</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add or remove an emoji reaction to a previously sent message.
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
from rcs.messages import MessageReactionSchemaOptions

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.messages.react(
    message_id=1410,
    options=MessageReactionSchemaOptions(
        force=True,
    ),
    reaction="👍",
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

**message_id:** `int` — Unique identifier of the message.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[MessageReactionSchemaOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**reaction:** `typing.Optional[str]` 

Unicode emoji to add. <br>

Use `null` to remove existing reaction.
    
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

## PhoneNumbers
<details><summary><code>client.phone_numbers.<a href="src/rcs/phone_numbers/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for available phone numbers that match your exact criteria.
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
from rcs.phone_numbers import (
    SearchSchemaLocation,
    SearchSchemaNumber,
    SearchSchemaOptions,
)

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.phone_numbers.search(
    features=["SMS", "MMS"],
    location=SearchSchemaLocation(
        city="New York",
        national_destination_code="212",
    ),
    phone_number_digit_filters=SearchSchemaNumber(
        contains="514",
        starts_with="45",
    ),
    options=SearchSchemaOptions(
        limit=4,
    ),
    type=["LOCAL"],
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

**type:** `typing.Sequence[PhoneEnum]` — Types of phone numbers to return in your search.
    
</dd>
</dl>

<dl>
<dd>

**features:** `typing.Optional[typing.Sequence[PhoneFeatureEnum]]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[SearchSchemaLocation]` 

Filter your search by geographic location to find numbers in specific regions. <br>

Toll-free numbers ignore city and state filters.
    
</dd>
</dl>

<dl>
<dd>

**phone_number_digit_filters:** `typing.Optional[SearchSchemaNumber]` — Filter your search by digit pattern.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[SearchSchemaOptions]` — Extra search settings to control how many results you get.
    
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

<details><summary><code>client.phone_numbers.<a href="src/rcs/phone_numbers/client.py">buy</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Purchase one or more phone numbers found through the [search endpoint](./search). <br>

Billing uses your account credits and the numbers are ready for immediate use.
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
client.phone_numbers.buy(
    numbers=["+18559491727"],
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

**numbers:** `typing.Sequence[str]` 

List of phone numbers you want to purchase, each in international E.164 format. <br>

All specified numbers must be currently available and will be validated for availability before processing the purchase. <br>

If any number in the request is unavailable or invalid, no purchases will be made and the request will be voided.
    
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

<details><summary><code>client.phone_numbers.<a href="src/rcs/phone_numbers/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve information about any phone number.
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
from rcs.phone_numbers import (
    PhoneDetailsSchemaOptions,
    PhoneDetailsSchemaOptionsEnhancedContactInfo,
)

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.phone_numbers.get(
    phone="+11234567890",
    level="advanced",
    options=PhoneDetailsSchemaOptions(
        risk=True,
        enhanced_contact_info=PhoneDetailsSchemaOptionsEnhancedContactInfo(
            context="This is my friend from JZ. He has done a lot in the crypto space.",
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

**phone:** `str` — Phone number you want to analyze in E.164 format.
    
</dd>
</dl>

<dl>
<dd>

**level:** `PhoneDetailsSchemaLevel` 

Choose how much detail you want in your results:
- `basic`: Receive essential info like carrier, location, and format.
- `advanced`: Receive a deeper analysis including fraud risk, detailed location, and enhanced contact info.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[PhoneDetailsSchemaOptions]` — Customize your lookup with additional options.
    
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

## Webhooks
<details><summary><code>client.webhooks.<a href="src/rcs/webhooks/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all webhook that are set up to receive events for specific URLs or phone numbers.
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
client.webhooks.get(
    identifiers=[
        "https://www.pinnacle.sh/payment",
        "+14155678901",
        "https://www.pinnacle.sh/sms-callback",
        "+14153456659",
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

**identifiers:** `typing.Sequence[str]` — List of URLs or phone numbers in E.164 format that the webhook is attached to.
    
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

## Campaigns Dlc
<details><summary><code>client.campaigns.dlc.<a href="src/rcs/campaigns/dlc/client.py">autofill</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate campaign details based off existing campaign and the brand it's connected to.
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
client.campaigns.dlc.autofill(
    additional_info="Please autofill missing DLC campaign fields using my brand profile",
    campaign_id=161,
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

**additional_info:** `typing.Optional[str]` — Any additional information you want to provide.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[int]` — Campaign ID.
    
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

<details><summary><code>client.campaigns.dlc.<a href="src/rcs/campaigns/dlc/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve DLC campaign.
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
client.campaigns.dlc.get(
    campaign_id=28,
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

**campaign_id:** `int` — Unique identifier of the DLC campaign.
    
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

<details><summary><code>client.campaigns.dlc.<a href="src/rcs/campaigns/dlc/client.py">submit</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit your DLC campaign for approval and activation with carriers.
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
client.campaigns.dlc.submit(
    campaign_id=161,
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

**campaign_id:** `int` — Unique identifier of the DLC campaign to submit.
    
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

<details><summary><code>client.campaigns.dlc.<a href="src/rcs/campaigns/dlc/client.py">upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new DLC campaign or updates an existing one. <br>

Omit campaignId to create a campaign.
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
from rcs.campaigns.dlc import (
    UpsertDlcSchemaKeywords,
    UpsertDlcSchemaKeywordsHelp,
    UpsertDlcSchemaKeywordsOptIn,
    UpsertDlcSchemaKeywordsOptOut,
    UpsertDlcSchemaLinks,
    UpsertDlcSchemaOptions,
    UpsertDlcSchemaUseCase,
)

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.campaigns.dlc.upsert(
    auto_renew=True,
    brand=1,
    campaign_id=161,
    keywords=UpsertDlcSchemaKeywords(
        help=UpsertDlcSchemaKeywordsHelp(
            message="Reply HELP for assistance, STOP to opt-out",
            values=["HELP", "INFO", "SUPPORT"],
        ),
        opt_in=UpsertDlcSchemaKeywordsOptIn(
            message="Welcome! You're now subscribed to Pinnacle.",
            values=["JOIN", "START", "SUBSCRIBE"],
        ),
        opt_out=UpsertDlcSchemaKeywordsOptOut(
            message="You've been unsubscribed. Reply START to rejoin.",
            values=["STOP", "QUIT", "UNSUBSCRIBE"],
        ),
    ),
    links=UpsertDlcSchemaLinks(
        privacy_policy="https://www.pinnacle.sh/privacy",
        terms_of_service="https://www.pinnacle.sh/terms",
    ),
    message_flow="Customer initiates -> Automated response -> Agent follow-up if needed",
    name="Account Notifications",
    options=UpsertDlcSchemaOptions(
        affiliate_marketing=False,
        age_gated=False,
        direct_lending=False,
        embedded_link="https://www.pinnacle.sh/example",
        embedded_phone=False,
        number_pooling=False,
    ),
    sample_messages=["Security alert: Unusual login detected from new device."],
    use_case=UpsertDlcSchemaUseCase(
        sub=["FRAUD_ALERT"],
        value="ACCOUNT_NOTIFICATION",
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

**auto_renew:** `typing.Optional[bool]` — Whether the campaign renews automatically.
    
</dd>
</dl>

<dl>
<dd>

**brand:** `typing.Optional[int]` — Brand id.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[int]` — Unique identifier for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the campaign.
    
</dd>
</dl>

<dl>
<dd>

**keywords:** `typing.Optional[UpsertDlcSchemaKeywords]` — Keyword response configuration.
    
</dd>
</dl>

<dl>
<dd>

**links:** `typing.Optional[UpsertDlcSchemaLinks]` — Legal documentation links.
    
</dd>
</dl>

<dl>
<dd>

**message_flow:** `typing.Optional[str]` — Describe the flow of how users will opt in to this campaign.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Display name of the campaign.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[UpsertDlcSchemaOptions]` — Campaign configuration options.
    
</dd>
</dl>

<dl>
<dd>

**sample_messages:** `typing.Optional[typing.Sequence[str]]` — Example messages for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**use_case:** `typing.Optional[UpsertDlcSchemaUseCase]` — Use case for the campaign.
    
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

<details><summary><code>client.campaigns.dlc.<a href="src/rcs/campaigns/dlc/client.py">validate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validate your DLC campaign configuration against carrier requirements and compliance rules.
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
client.campaigns.dlc.validate(
    additional_info="Please validate this DLC campaign for 10DLC compliance",
    campaign_id=161,
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

**campaign_id:** `int` — Campaign ID.
    
</dd>
</dl>

<dl>
<dd>

**additional_info:** `typing.Optional[str]` — Any additional information you want to provide.
    
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

## Campaigns TollFree
<details><summary><code>client.campaigns.toll_free.<a href="src/rcs/campaigns/toll_free/client.py">autofill</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate campaign details based off existing campaign and the brand it's connected to.
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
client.campaigns.toll_free.autofill(
    additional_info="Please autofill missing DLC campaign fields using my brand profile",
    campaign_id=161,
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

**additional_info:** `typing.Optional[str]` — Any additional information you want to provide.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[int]` — Campaign ID.
    
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

<details><summary><code>client.campaigns.toll_free.<a href="src/rcs/campaigns/toll_free/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve Toll-Free campaign.
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
client.campaigns.toll_free.get(
    campaign_id=161,
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

**campaign_id:** `int` — Unique identifier of toll-free campaign.
    
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

<details><summary><code>client.campaigns.toll_free.<a href="src/rcs/campaigns/toll_free/client.py">submit</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit your toll-free campaign for approval and activation with carriers.
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
client.campaigns.toll_free.submit(
    campaign_id=161,
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

**campaign_id:** `int` — Unique identifier of the toll-free campaign to submit.
    
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

<details><summary><code>client.campaigns.toll_free.<a href="src/rcs/campaigns/toll_free/client.py">upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new toll-free campaign or updates an existing one.<br>

Omit campaignId to create a campaign.
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
from rcs.campaigns.toll_free import (
    UpsertTollFreeSchemaOptIn,
    UpsertTollFreeSchemaUseCase,
)

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.campaigns.toll_free.upsert(
    brand=2,
    campaign_id=161,
    monthly_volume="1,000",
    name="Pinnacle",
    opt_in=UpsertTollFreeSchemaOptIn(
        method="DIGITAL",
        url="https://www.pinnacle.sh/",
        workflow_description="Visit https://www.pinnacle.sh/",
    ),
    production_message_content="Join Pinnacle's workshop tomorrow and send your first RCS!",
    use_case=UpsertTollFreeSchemaUseCase(
        summary="Alerts clients about any Pinnacle hosted workshops.",
        value="WORKSHOP_ALERTS",
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

**brand:** `typing.Optional[int]` — Brand id.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[int]` — Unique identifier for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**monthly_volume:** `typing.Optional[MessageVolumeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Display name of the campaign.
    
</dd>
</dl>

<dl>
<dd>

**opt_in:** `typing.Optional[UpsertTollFreeSchemaOptIn]` — Opt-in keyword settings.
    
</dd>
</dl>

<dl>
<dd>

**production_message_content:** `typing.Optional[str]` — Explain message that would be sent.
    
</dd>
</dl>

<dl>
<dd>

**use_case:** `typing.Optional[UpsertTollFreeSchemaUseCase]` — Use case classification for the campaign.
    
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

<details><summary><code>client.campaigns.toll_free.<a href="src/rcs/campaigns/toll_free/client.py">validate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validate your toll-free campaign configuration against carrier requirements and compliance rules.
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
client.campaigns.toll_free.validate(
    additional_info="Please validate this DLC campaign for 10DLC compliance",
    campaign_id=161,
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

**campaign_id:** `int` — Campaign ID.
    
</dd>
</dl>

<dl>
<dd>

**additional_info:** `typing.Optional[str]` — Any additional information you want to provide.
    
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

## Campaigns Rcs
<details><summary><code>client.campaigns.rcs.<a href="src/rcs/campaigns/rcs/client.py">autofill</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate campaign details based off existing campaign and the brand it's connected to.
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
client.campaigns.rcs.autofill(
    additional_info="Please autofill missing DLC campaign fields using my brand profile",
    campaign_id=161,
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

**additional_info:** `typing.Optional[str]` — Any additional information you want to provide.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[int]` — Campaign ID.
    
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

<details><summary><code>client.campaigns.rcs.<a href="src/rcs/campaigns/rcs/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve RCS campaign.
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
client.campaigns.rcs.get(
    campaign_id=161,
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

**campaign_id:** `int` — Unique identifier of the RCS campaign.
    
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

<details><summary><code>client.campaigns.rcs.<a href="src/rcs/campaigns/rcs/client.py">submit</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit your RCS campaign for approval and activation with carriers.
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
client.campaigns.rcs.submit(
    campaign_id=161,
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

**campaign_id:** `int` — Unique identifier of the RCS campaign to retrieve.
    
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

<details><summary><code>client.campaigns.rcs.<a href="src/rcs/campaigns/rcs/client.py">upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new RCS campaign or updates an existing one. <br>

Omit campaignId to create a campaign.
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
from rcs.campaigns.rcs import (
    UpsertRcsSchemaAgent,
    UpsertRcsSchemaAgentEmailsItem,
    UpsertRcsSchemaAgentPhonesItem,
    UpsertRcsSchemaAgentWebsitesItem,
    UpsertRcsSchemaLinks,
    UpsertRcsSchemaOptIn,
    UpsertRcsSchemaOptOut,
    UpsertRcsSchemaUseCase,
)

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.campaigns.rcs.upsert(
    agent=UpsertRcsSchemaAgent(
        color="#000000",
        description="Engaging campaigns with RBM – next-gen SMS marketing with rich content and better analytics.",
        emails=[
            UpsertRcsSchemaAgentEmailsItem(
                email="founders@trypinnacle.app",
                label="Email Us",
            )
        ],
        hero_url="https://agent-logos.storage.googleapis.com/_/m0bk9mmw7kfynqiKSPfsaoc6",
        icon_url="https://agent-logos.storage.googleapis.com/_/m0bk9gvlDunZEw1krfruZmw3",
        name="Pinnacle Software Development",
        phones=[
            UpsertRcsSchemaAgentPhonesItem(
                label="Contact us directly",
                phone="+14154467821",
            )
        ],
        websites=[
            UpsertRcsSchemaAgentWebsitesItem(
                label="Get started with Pinnacle",
                url="https://www.trypinnacle.app/",
            )
        ],
    ),
    brand=2,
    expected_agent_responses=[
        "Here are the things I can help you with.",
        "I can assist you with booking an appointment, or you may choose to book manually.",
        "Here are the available times to connect with a representative tomorrow.",
        "Your appointment has been scheduled.",
    ],
    links=UpsertRcsSchemaLinks(
        privacy_policy="https://www.trypinnacle.app/privacy",
        terms_of_service="https://www.trypinnacle.app/terms",
    ),
    opt_in=UpsertRcsSchemaOptIn(
        method="WEBSITE",
        terms_and_conditions="Would you like to subscribe to Pinnacle?",
    ),
    opt_out=UpsertRcsSchemaOptOut(
        description="Reply STOP to opt-out anytime.",
        keywords=["STOP", "UNSUBSCRIBE", "END"],
    ),
    use_case=UpsertRcsSchemaUseCase(
        behavior="Acts as a customer service representative.",
        value="OTHER",
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

**agent:** `typing.Optional[UpsertRcsSchemaAgent]` — Create an agent for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**brand:** `typing.Optional[int]` — Unique identifier for the brand.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[int]` — Unique identifier for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**expected_agent_responses:** `typing.Optional[typing.Sequence[str]]` — List of what the agent might say to users (1-5 required).
    
</dd>
</dl>

<dl>
<dd>

**links:** `typing.Optional[UpsertRcsSchemaLinks]` — Legal documentation links.
    
</dd>
</dl>

<dl>
<dd>

**opt_in:** `typing.Optional[UpsertRcsSchemaOptIn]` — Opt-in configuration.
    
</dd>
</dl>

<dl>
<dd>

**opt_out:** `typing.Optional[UpsertRcsSchemaOptOut]` — Opt-out configuration.
    
</dd>
</dl>

<dl>
<dd>

**use_case:** `typing.Optional[UpsertRcsSchemaUseCase]` — Use case classification for the campaign.
    
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

<details><summary><code>client.campaigns.rcs.<a href="src/rcs/campaigns/rcs/client.py">validate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validate your RCS campaign configuration against carrier requirements and compliance rules.
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
client.campaigns.rcs.validate(
    additional_info="Please validate this DLC campaign for 10DLC compliance",
    campaign_id=161,
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

**campaign_id:** `int` — Campaign ID.
    
</dd>
</dl>

<dl>
<dd>

**additional_info:** `typing.Optional[str]` — Any additional information you want to provide.
    
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

## Messages Sms
<details><summary><code>client.messages.sms.<a href="src/rcs/messages/sms/client.py">send</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a SMS message immediately or schedule it for future delivery.
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
client.messages.sms.send(
    from_="+14155164736",
    text="Hey! 😂",
    to="+14154746461",
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

**from_:** `str` — Phone number that sends the message in E.164 format.
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Message content.
    
</dd>
</dl>

<dl>
<dd>

**to:** `str` — Recipient's phone number in E.164 format.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[SendSmsSchemaOptions]` — Additional settings to customize SMS delivery.
    
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

<details><summary><code>client.messages.sms.<a href="src/rcs/messages/sms/client.py">validate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validate SMS message content without sending it.
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
client.messages.sms.validate(
    text="Hello from Pinnacle",
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

**text:** `str` — Message content.
    
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

## Messages Mms
<details><summary><code>client.messages.mms.<a href="src/rcs/messages/mms/client.py">send</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a MMS immediately or schedule it for future delivery.
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
from rcs.messages.mms import SendMmsSchemaOptions

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.messages.mms.send(
    from_="+14155164736",
    media_urls=[
        "https://fastly.picsum.photos/id/941/300/300.jpg?hmac=mDxM9PWSqRDjecwSCEpzU4bj35gqnG7yA25OL29uNv0"
    ],
    options=SendMmsSchemaOptions(
        multiple_messages=True,
        validate=True,
    ),
    text="Check out this image!",
    to="+14154746461",
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

**from_:** `str` — Phone number you want to send the message from in E.164 format.
    
</dd>
</dl>

<dl>
<dd>

**media_urls:** `typing.Sequence[str]` 

Media file URLs to send.<br>

 See [supported media types](https://app.pinnacle.sh/supported-file-types?type=MMS).
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Message text to accompany the media.
    
</dd>
</dl>

<dl>
<dd>

**to:** `str` — Recipient's phone number in E.164 format.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[SendMmsSchemaOptions]` — Control how your MMS is processed and delivered.
    
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

<details><summary><code>client.messages.mms.<a href="src/rcs/messages/mms/client.py">validate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validate MMS message content without sending it.
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
client.messages.mms.validate(
    media_urls=[
        "https://upload.wikimedia.org/wikipedia/commons/b/b9/Pizigani_1367_Chart_1MB.jpg",
        "https://fastly.picsum.photos/id/528/1000/1000.jpg?hmac=aTG0xNif9KbNryFN0ZNZ_nFK6aEpZxqUGCZF1KjOT8w",
        "https://file-examples.com/storage/fefdd7ab126835e7993bb1a/2017/10/file_example_JPG_500kB.jpg",
    ],
    text="Check out these images!",
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

**media_urls:** `typing.Sequence[str]` 

URLs of media files in this message. <br>

See [supported media types](https://app.pinnacle.sh/supported-file-types?type=MMS).
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` — Text content that accompanies the media files.
    
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

## Messages Rcs
<details><summary><code>client.messages.rcs.<a href="src/rcs/messages/rcs/client.py">send</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a RCS message immediately or schedule it for future delivery. <br>

Requires an active RCS agent and recipient devices that support RCS Business Messaging.
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
from rcs import Pinnacle, RcsButtonContent_OpenUrl, RcsText

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.messages.rcs.send(
    request=RcsText(
        quick_replies=[
            RcsButtonContent_OpenUrl(
                payload="payload",
                title="title",
            )
        ],
        text="text",
        from_="from",
        to="to",
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

**request:** `Rcs` 
    
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

<details><summary><code>client.messages.rcs.<a href="src/rcs/messages/rcs/client.py">validate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validate RCS message content without sending it.
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
from rcs import Pinnacle, RcsButtonContent_OpenUrl, RcsTextContent

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.messages.rcs.validate(
    request=RcsTextContent(
        quick_replies=[
            RcsButtonContent_OpenUrl(
                payload="payload",
                title="title",
            )
        ],
        text="text",
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

**request:** `RcsValidateContent` 
    
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

## PhoneNumbers Webhook
<details><summary><code>client.phone_numbers.webhook.<a href="src/rcs/phone_numbers/webhook/client.py">attach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Connect a webhook to your phone number to receive real-time notifications for incoming messages, delivery status updates, and other communication events.
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
from rcs import AttachWebhookSchemaWebhookId, Pinnacle

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.phone_numbers.webhook.attach(
    phone="%2B14155551234",
    request=AttachWebhookSchemaWebhookId(
        webhook_id=1,
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

**phone:** `str` 

The phone number you want to attach the webhook to in E.164 format. Make sure it is url encoded (i.e. replace the leading + with %2B). <br>

Must be a phone number that you own and have already [purchased](./buy) through the API.
    
</dd>
</dl>

<dl>
<dd>

**request:** `AttachWebhookParams` 
    
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

<details><summary><code>client.phone_numbers.webhook.<a href="src/rcs/phone_numbers/webhook/client.py">detach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disconnect a webhook from your phone number to stop receiving event notifications for that specific number. <br>

The webhook configuration itself remains intact and available for use with other phone numbers.
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
client.phone_numbers.webhook.detach(
    phone="+14155551234",
    webhook_id=123,
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

**phone:** `str` 

The phone number you want to attach the webhook to in E.164 format. Make sure it is url encoded (i.e. replace the leading + with %2B). <br>

Must be a phone number that you own and currently has the specified webhook attached.
    
</dd>
</dl>

<dl>
<dd>

**webhook_id:** `int` 

The unique identifier of the webhook you want to detach from the phone number. <br>

This must be a valid webhook ID that is currently attached to the specified phone number.
    
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

## PhoneNumbers Campaign
<details><summary><code>client.phone_numbers.campaign.<a href="src/rcs/phone_numbers/campaign/client.py">attach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Link a phone number to a specific campaign.
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
client.phone_numbers.campaign.attach(
    phones=["+14155550123", "+14155559876", "+14155550111"],
    campaign_type="TOLL_FREE",
    campaign_id=101,
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

**phones:** `typing.Sequence[str]` — List of phone number (E.164 format).
    
</dd>
</dl>

<dl>
<dd>

**campaign_type:** `MessagingProfileEnum` 
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `int` — Campaign's identifier.
    
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

<details><summary><code>client.phone_numbers.campaign.<a href="src/rcs/phone_numbers/campaign/client.py">detach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove the association between a phone number and its attached campaign.
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
client.phone_numbers.campaign.detach(
    phones=["+14155559876", "14155550111"],
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

**phones:** `typing.Sequence[str]` — List of phone numbers (E.164 format).
    
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

## Status Get
<details><summary><code>client.status.get.<a href="src/rcs/status/get/client.py">brand</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a brand's status.
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
client.status.get.brand(
    brand_id=28,
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

**brand_id:** `int` — ID of the brand.
    
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

<details><summary><code>client.status.get.<a href="src/rcs/status/get/client.py">toll_free</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a toll-free campaign's status.
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
client.status.get.toll_free(
    campaign_id=28,
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

**campaign_id:** `int` — ID of the toll-free campaign.
    
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

<details><summary><code>client.status.get.<a href="src/rcs/status/get/client.py">dlc</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a DLC campaign's status.
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
client.status.get.dlc(
    campaign_id=28,
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

**campaign_id:** `int` — ID of the DLC campaign.
    
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

<details><summary><code>client.status.get.<a href="src/rcs/status/get/client.py">rcs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a RCS campaign's status.
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
client.status.get.rcs(
    campaign_id=28,
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

**campaign_id:** `int` — ID of the campaign.
    
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

<details><summary><code>client.status.get.<a href="src/rcs/status/get/client.py">phone_number</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a phone number's order status and campaign attachment status. <br>

Check if a number is active and ready to send messages.
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
client.status.get.phone_number(
    phone_number="+14151234567",
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

**phone_number:** `str` — Phone number in E164 format that is in review.
    
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

## Tools Url
<details><summary><code>client.tools.url.<a href="src/rcs/tools/url/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a shortened URL that redirects visitors to the provided destination URL.
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
from rcs import CreateUrlOptions, Pinnacle

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.tools.url.create(
    url="https://www.pinnacle.sh/",
    options=CreateUrlOptions(
        expires_at="2025-06-23T16:18:25.000Z",
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

**url:** `str` — Destination URL for the shortened link that visitors will be redirected to when clicked.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[CreateUrlOptions]` 
    
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

<details><summary><code>client.tools.url.<a href="src/rcs/tools/url/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve configuration and details for your shortened URL using its unique identifier.
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
client.tools.url.get(
    link_id="ePzVxILF",
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

**link_id:** `str` 

Unique identifier from your shortened URL. For example, for `https://pncl.to/ePzVxILF`, the `linkId` is `ePzVxILF`. <br>

See the response of [Create Shortened URL](./create-url) for more information. 
    
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

<details><summary><code>client.tools.url.<a href="src/rcs/tools/url/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the destination or configuration of an existing shortened URL.
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
client.tools.url.update(
    link_id="ePzVxILF",
    url="https://www.pinnacle.sh/",
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

**link_id:** `str` 

Unique identifier from your shortened URL. For example, for `https://pncl.to/ePzVxILF`, the `linkId` is `ePzVxILF`. <br>

See the response of [Create Shortened URL](./create-url) for more information. 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — New destination URL where your visitors will be redirected.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[CreateUrlOptions]` 
    
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

## Tools File
<details><summary><code>client.tools.file.<a href="src/rcs/tools/file/client.py">upload</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate presigned URLs that let you upload files directly to our storage and allow your users to download them securely.
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
from rcs.tools.file import (
    FileUploadSchemaOptions,
    FileUploadSchemaOptionsDownload,
)

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.tools.file.upload(
    content_type="image/jpeg",
    size=1024,
    name="test.jpg",
    options=FileUploadSchemaOptions(
        download=FileUploadSchemaOptionsDownload(
            expires_at="2025-06-30T12:00:00.000Z",
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

**content_type:** `str` 

MIME type of your file. <br>

Supported file types:
- Audio: mp3, mp4, mpeg, ogg, aac, webm, wav, 3gpp, amr
- Video: mp4, mpeg, quicktime, webm, 3gpp, H.264, m4v
- Image: jpeg, png, gif, bmp, tiff, webp
- Documents: pdf, csv, rtf, calendar, vcard
    
</dd>
</dl>

<dl>
<dd>

**size:** `int` — Size of your file in bytes. Should be less than 100 MB.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of your file.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[FileUploadSchemaOptions]` — Additional configurations for your file.
    
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

## Tools ContactCard
<details><summary><code>client.tools.contact_card.<a href="src/rcs/tools/contact_card/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve contact information as a vCard and get a presigned URL to download the file.
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
client.tools.contact_card.get(
    id=33,
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

**id:** `int` — ID of your contact.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[GetVCardSchemaOptions]` 
    
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

<details><summary><code>client.tools.contact_card.<a href="src/rcs/tools/contact_card/client.py">upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new contact card or updates an existing one with full vCard data.
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
from rcs import (
    Pinnacle,
    VcardAddress,
    VcardEmail,
    VCardGeo,
    VCardName,
    VCardOrganization,
    VcardPhone,
)

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.tools.contact_card.upsert(
    id=34,
    formatted_name="Jane Smith",
    name=VCardName(
        family_name="Smith",
        given_name="Jane",
        additional_names=["A."],
        honorific_prefixes=["Dr."],
        honorific_suffixes=["PhD"],
    ),
    nickname=["Janie"],
    birthday="1990-02-15",
    addresses=[
        VcardAddress(
            country_name="USA",
            extended_address="Apt. 4B",
            locality="Anytown",
            postal_code="90210",
            post_office_box="PO Box 123",
            region="CA",
            street_address="123 Main St",
            type=["HOME", "PREF"],
        )
    ],
    url="https://app.pinnacle.sh",
    phones=[
        VcardPhone(
            type=["CELL"],
            value="+15551234567",
        )
    ],
    emails=[
        VcardEmail(
            type=["INTERNET"],
            value="jane.smith@example.com",
        )
    ],
    timezone="America/Los_Angeles",
    geo=VCardGeo(
        latitude=34.0522,
        longitude=-118.2437,
    ),
    title="Engineer",
    role="Developer",
    organization=VCardOrganization(
        name="Acme Co",
        units=["Engineering", "R&D"],
    ),
    categories=["Friend", "Colleague"],
    note="Test contact entry",
    photo="https://fastly.picsum.photos/id/853/200/200.jpg?hmac=f4LF-tVBBnJb9PQAVEO8GCTGWgLUnxQLw44rUofE6mQ",
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

**photo:** `typing.Optional[str]` — Contact's photo
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` — Unique identifier for the contact.
    
</dd>
</dl>

<dl>
<dd>

**formatted_name:** `typing.Optional[str]` — Full display name for the vCard.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[VCardName]` — Structured name components.
    
</dd>
</dl>

<dl>
<dd>

**nickname:** `typing.Optional[typing.Sequence[str]]` — Nicknames or aliases.
    
</dd>
</dl>

<dl>
<dd>

**birthday:** `typing.Optional[str]` — Birthday in ISO 8601 date format (YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[VcardAddress]]` — Physical addresses.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — Website URL.
    
</dd>
</dl>

<dl>
<dd>

**phones:** `typing.Optional[typing.Sequence[VcardPhone]]` — Phone numbers.
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[VcardEmail]]` — Email addresses.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — Timezone (e.g., "America/New_York").
    
</dd>
</dl>

<dl>
<dd>

**geo:** `typing.Optional[VCardGeo]` — Geographic coordinates.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Job title or position.
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` — Role or function within the organization.
    
</dd>
</dl>

<dl>
<dd>

**organization:** `typing.Optional[VCardOrganization]` — Organization or company information.
    
</dd>
</dl>

<dl>
<dd>

**categories:** `typing.Optional[typing.Sequence[str]]` — Categories or tags for organizing contacts.
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` — Additional notes or comments.
    
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

