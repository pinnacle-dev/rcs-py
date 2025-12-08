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
from rcs.brands import AutofillBrandOptions

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.brands.autofill(
    additional_info="A developer-friendly, compliant API for SMS, MMS, and RCS, built to scale real conversations.",
    name="Pinnacle",
    options=AutofillBrandOptions(
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

**options:** `typing.Optional[AutofillBrandOptions]` 
    
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
from rcs import Pinnacle, UpsertContact

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.brands.upsert(
    address="500 Folsom St, San Francisco, CA 94105",
    contact=UpsertContact(
        email="michael.chen@trypinnacle.app",
        name="Michael Chen",
        phone="+14155551234",
        title="Customer Support Representative",
    ),
    dba="Pinnacle RCS",
    description="A developer-friendly, compliant API for SMS, MMS, and RCS, built to scale real conversations.",
    ein="88-1234567",
    email="founders@trypinnacle.app",
    id="b_1234567890",
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

**contact:** `typing.Optional[UpsertContact]` — Contact information for the brand.
    
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

**id:** `typing.Optional[str]` 

The unique identifier of the brand you want to update.
<br><br> This identifier is a string that always begins with the prefix `b_`, for example: `b_1234567890`.
    
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
    id="b_1234567890",
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

**id:** `str` 

The unique identifier of the brand you want to retrieve from your account.
<br><br> This identifier is a string that always begins with the prefix `b_`, for example: `b_1234567890`.
    
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
    brand_id="b_1234567890",
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

**brand_id:** `str` 

The unique identifier of the brand you want to submit for review. <br><br>
This identifier is a string that always begins with the prefix `b_`, for example: `b_1234567890` and must correspond to an existing brand in your account that is ready for submission.
    
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
    brand_id="b_1234567890",
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

**brand_id:** `str` 

The unique identifier of the brand to vet. <br>

This identifier is a string that always begins with the prefix `b_`, for example: `b_1234567890` and must correspond to an existing brand in your account that is ready for vetting.
    
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

## Audiences
<details><summary><code>client.audiences.<a href="src/rcs/audiences/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an audience by ID with optional pagination.
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
client.audiences.get(
    id="aud_abc123",
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

**id:** `str` — Audience ID. This identifier is a string that always begins with the prefix `aud_`, for example: `aud_abc123`.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number. If provided with or without limit, returns paginated contacts.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Items per page. If provided with or without page, returns paginated contacts.
    
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

<details><summary><code>client.audiences.<a href="src/rcs/audiences/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new audience with optional initial contacts. Phone numbers that don't exist will be auto-created as contacts.
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
client.audiences.create(
    name="Mixed Audience",
    contacts=["+12125551234", "co_abc123", "+13105551234"],
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

**name:** `str` — Audience name.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Audience description.
    
</dd>
</dl>

<dl>
<dd>

**contacts:** `typing.Optional[typing.Sequence[str]]` — Optional array of phone numbers (E.164 format) or contact IDs.
    
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

<details><summary><code>client.audiences.<a href="src/rcs/audiences/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete an audience and all its contact associations.

Note: This will NOT delete the contacts themselves, only the audience and its memberships.
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
client.audiences.delete(
    id="aud_abc123",
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

**id:** `str` — Audience ID. This identifier is a string that always begins with the prefix `aud_`, for example: `aud_abc123`.
    
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

<details><summary><code>client.audiences.<a href="src/rcs/audiences/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update audience metadata. This endpoint does NOT modify contacts.

To add or remove contacts, use the [Add Contacts](/api-reference/audiences/add-contacts) or [Remove Contacts](/api-reference/audiences/remove-contacts) endpoints.
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
client.audiences.update(
    id="aud_abc123",
    name="Updated Audience Name",
    description="New description",
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

**id:** `str` — Audience ID to update. This identifier is a string that always begins with the prefix `aud_`, for example: `aud_abc123`.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — New audience name.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — New audience description.
    
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
client.contacts.get(
    id="co_1234567890",
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

**id:** `typing.Optional[str]` 

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
    id="co_1234567890",
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

**id:** `str` — ID of the contact you want to update. This identifier is a string that always begins with the prefix `co_`, for example: `co_1234567890`.
    
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
from rcs import ConversationByIdParams, Pinnacle

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.conversations.get(
    request=ConversationByIdParams(
        id="conv_1234567890",
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
    brand_id="b_1234567890",
    campaign_id="tf_1234567890",
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

**brand_id:** `typing.Optional[str]` — The unique identifier of the brand to filter conversations. This identifier is a string that always begins with the prefix `b_`, for example: `b_1234567890`.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` 

The unique identifier of the campaign to filter conversations. This identifier is a string that begins with the prefix: 
- TOLL_FREE: `tf_` (e.g., `tf_1234567890`)
- 10DLC: `dlc_` (e.g., `dlc_1234567890`)
- RCS: `rcs_` (e.g., `rcs_1234567890`)
    
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
    id="conv_1234567890",
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

**id:** `str` — The unique identifier of the conversation to update. This identifier is a string that always begins with the prefix `conv_`, for example: `conv_1234567890`.
    
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

<details><summary><code>client.conversations.<a href="src/rcs/conversations/client.py">list_messages</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a paginated and filtered list of messages for a specific conversation.
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
client.conversations.list_messages(
    id="id",
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

**id:** `str` — Unique identifier of the conversation. This identifier is a string that always begins with the prefix `conv_`, for example: `conv_1234567890`.
    
</dd>
</dl>

<dl>
<dd>

**page_index:** `typing.Optional[int]` — Zero-based index for pagination.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of messages to return per page.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListMessagesConversationsRequestSortOrder]` 

Sort order for messages. <br>

- `asc`: Oldest messages first
- `desc`: Newest messages first (default)
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[ListMessagesConversationsRequestDirection]` 

Filter messages by direction. <br>

- `INBOUND`: Messages received from contacts
- `OUTBOUND`: Messages sent to contacts
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListMessagesConversationsRequestStatus]` — Filter messages by delivery status.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ListMessagesConversationsRequestType]` — Filter messages by protocol type.
    
</dd>
</dl>

<dl>
<dd>

**date_from:** `typing.Optional[dt.datetime]` — Filter messages sent on or after this date (ISO 8601 format).
    
</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[dt.datetime]` — Filter messages sent on or before this date (ISO 8601 format).
    
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
    id="msg_1234567890",
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

**id:** `str` — Unique identifier of the message. This identifier is a string that always begins with the prefix `msg_`, for example: `msg_1234567890`.
    
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
from rcs.messages import ReactMessageOptions

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.messages.react(
    message_id="msg_1234567890",
    options=ReactMessageOptions(
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

**message_id:** `str` — Unique identifier of the message. This identifier is a string that always begins with the prefix `msg_`, for example: `msg_1234567890`.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[ReactMessageOptions]` 
    
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

<details><summary><code>client.messages.<a href="src/rcs/messages/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a previously scheduled message before it is sent.

Use the `scheduleId` returned from a scheduled send request (SMS, MMS, or RCS) to cancel the message.
Once cancelled, the scheduled message will stop being sent.

> **Note:** You cannot cancel a message that has already been sent.
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
client.messages.cancel(
    id="msg_sched_1234567890",
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

**id:** `str` — Unique identifier of the scheduled message. This identifier is a string that always begins with the prefix `msg_sched_`, for example: `msg_sched_1234567890`.
    
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
    SearchPhoneNumberByDigits,
    SearchPhoneNumberByLocation,
    SearchPhoneNumberOptions,
)

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.phone_numbers.search(
    features=["SMS", "MMS"],
    location=SearchPhoneNumberByLocation(
        city="New York",
        national_destination_code="212",
    ),
    number=SearchPhoneNumberByDigits(
        contains="514",
        starts_with="45",
    ),
    options=SearchPhoneNumberOptions(
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

**location:** `typing.Optional[SearchPhoneNumberByLocation]` 

Filter your search by geographic location to find numbers in specific regions. <br>

Toll-free numbers ignore city and state filters.
    
</dd>
</dl>

<dl>
<dd>

**number:** `typing.Optional[SearchPhoneNumberByDigits]` — Filter your search by digit pattern.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[SearchPhoneNumberOptions]` — Extra search settings to control how many results you get.
    
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
    EnhancedContactInfo,
    RetrievePhoneNumberDetailsOptions,
)

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.phone_numbers.get(
    phone="+11234567890",
    level="advanced",
    options=RetrievePhoneNumberDetailsOptions(
        risk=True,
        enhanced_contact_info=EnhancedContactInfo(
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

**options:** `typing.Optional[RetrievePhoneNumberDetailsOptions]` — Customize your lookup with additional options.
    
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

## RCS
<details><summary><code>client.rcs.<a href="src/rcs/rcs/client.py">get_capabilities</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check RCS capabilities for one or more phone numbers.

This endpoint allows you to verify which RCS features (cards, buttons, etc.) are supported
on specific phone numbers before sending RCS messages to them.
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
client.rcs.get_capabilities(
    phone_numbers=["+12345678901", "+19876543210"],
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

**phone_numbers:** `typing.Sequence[str]` — List of phone numbers to check RCS capabilities for (E.164 format)
    
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

<details><summary><code>client.rcs.<a href="src/rcs/rcs/client.py">whitelist</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Whitelist a phone number for testing with your test RCS agent.

## Overview
During development and testing, RCS agents can only send messages to whitelisted phone numbers.
Use this endpoint to whitelist specific phone numbers to send and receive messages from the test agent.

## Verification Process
After whitelisting a number, you'll need to complete verification:

1. Check the test device for message from "RBM Tester Management"
2. Click the "Make me a tester" button
3. Enter the separate 4-digit verification SMS code in the Pinnacle dashboard at:
   ```
   https://app.pinnacle.sh/dashboard/brands/{brandId}?campaignId={campaignId}&campaignType=RCS
   ```

 > **⚠️ Important: Re-whitelisting Numbers**
>
> If you whitelist a number that's already whitelisted, you'll receive a new message from "RBM Tester Management". **You must click the "Make me a tester" button again to continue sending and receiving messages.**

> **Important Notes**
>
> - **Verification required:** Messages cannot be sent nor received until you have clicked the "Make me a tester" button on the test device.
> - **Testing only:** This is only required for test agents. Production agents can message any RCS-enabled number.
> - **Network limitations:** Whitelisting may be temporarily unavailable for some carriers but are usually restored shortly.
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
client.rcs.whitelist(
    agent_id="agent_XXXXXXXXXXXX",
    phone_number="+12345678901",
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

**agent_id:** `str` — The RCS agent ID (must be prefixed with 'agent_')
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `str` — Phone number to whitelist for testing (E.164 format)
    
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

<details><summary><code>client.rcs.<a href="src/rcs/rcs/client.py">get_link</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a link for initiating an RCS conversation with your agent. 

Users can click these links to start conversations with your RCS agent directly
from websites, emails, or other applications.
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
client.rcs.get_link(
    agent_id="agent_XXXXXXXXXXXX",
    test_mode=False,
    phone_number="+12345678901",
    body="Hello, I need help with my order",
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

**agent_id:** `str` — The RCS agent ID (must be prefixed with 'agent_')
    
</dd>
</dl>

<dl>
<dd>

**test_mode:** `typing.Optional[bool]` — Link to the test agent or the production agent if false
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — Fallback phone number (E.164 format) to use if the phone number does not support RCS. If not provided, no url will be generated.
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` — Optional message body to pre-fill after the user clicks the link
    
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

## Audiences Contacts
<details><summary><code>client.audiences.contacts.<a href="src/rcs/audiences/contacts/client.py">remove</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove contacts from an existing audience. This operation is idempotent.

- Only removes contacts that exist in the audience
- Contacts not in the audience are ignored
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
client.audiences.contacts.remove(
    id="aud_abc123",
    contacts=["+12125551234", "co_def456"],
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

**id:** `str` — Audience ID. This identifier is a string that always begins with the prefix `aud_`, for example: `aud_abc123`.
    
</dd>
</dl>

<dl>
<dd>

**contacts:** `typing.Sequence[str]` — Array of phone numbers (E.164 format) or contact IDs (minimum 1 item).
    
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

<details><summary><code>client.audiences.contacts.<a href="src/rcs/audiences/contacts/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add contacts to an existing audience. This operation is additive and idempotent.

- Phone numbers that don't exist will be auto-created as contacts
- Duplicate adds are ignored
- Contacts already in the audience are ignored
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
client.audiences.contacts.add(
    id="aud_abc123",
    contacts=["+12125551234", "co_def456", "+13105551234"],
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

**id:** `str` — Audience ID. This identifier is a string that always begins with the prefix `aud_`, for example: `aud_abc123`.
    
</dd>
</dl>

<dl>
<dd>

**contacts:** `typing.Sequence[str]` — Array of phone numbers (E.164 format) or contact IDs (minimum 1 item).
    
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
    additional_info="Please autofill missing campaign fields using my brand profile",
    campaign_id="dlc_1234567890",
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

**campaign_id:** `typing.Optional[str]` 

Unique identifier for the campaign.
- When autofilling 10DLC campaigns, it must begin with the prefix `dlc_` (e.g., `dlc_1234567890`)
- When autofilling Toll-Free campaigns, it must begin with the prefix `tf_` (e.g., `tf_1234567890`)
- When autofilling RCS campaigns, it must begin with the prefix `rcs_` (e.g., `rcs_1234567890`)
    
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

Retrieve 10DLC campaign.
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
    campaign_id="dlc_1234567890",
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

**campaign_id:** `str` — Unique identifier of the 10DLC campaign. This identifier is a string that always begins with the prefix `dlc_`, for example: `dlc_1234567890`.
    
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

Submit your 10DLC campaign for approval and activation with carriers.
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
    campaign_id="dlc_1234567890",
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

**campaign_id:** `str` 

Unique identifier of the 10DLC campaign to submit.
<br><br> This identifier is a string that always begins with the prefix `dlc_`, for example: `dlc_1234567890`.
    
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

Create a new 10DLC campaign or updates an existing one. <br>

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
    UpsertDlcCampaignHelpKeywords,
    UpsertDlcCampaignKeywords,
    UpsertDlcCampaignLinks,
    UpsertDlcCampaignOptInKeywords,
    UpsertDlcCampaignOptions,
    UpsertDlcCampaignOptOutKeywords,
    UpsertDlcCampaignUseCase,
)

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.campaigns.dlc.upsert(
    auto_renew=True,
    brand="b_1234567890",
    campaign_id="dlc_1234567890",
    keywords=UpsertDlcCampaignKeywords(
        help=UpsertDlcCampaignHelpKeywords(
            message="Reply HELP for assistance, STOP to opt-out",
            values=["HELP", "INFO", "SUPPORT"],
        ),
        opt_in=UpsertDlcCampaignOptInKeywords(
            message="Welcome. You are now subscribed to Pinnacle.",
            values=["JOIN", "START", "SUBSCRIBE"],
        ),
        opt_out=UpsertDlcCampaignOptOutKeywords(
            message="You have been unsubscribed. Reply START to rejoin.",
            values=["STOP", "QUIT", "UNSUBSCRIBE"],
        ),
    ),
    links=UpsertDlcCampaignLinks(
        privacy_policy="https://www.pinnacle.sh/privacy",
        terms_of_service="https://www.pinnacle.sh/terms",
    ),
    message_flow="Customer initiates -> Automated response -> Agent follow-up if needed",
    name="Account Notifications",
    options=UpsertDlcCampaignOptions(
        affiliate_marketing=False,
        age_gated=False,
        direct_lending=False,
        embedded_link="https://www.pinnacle.sh/example",
        embedded_phone=False,
        number_pooling=False,
    ),
    sample_messages=["Security alert: Unusual login detected from new device."],
    use_case=UpsertDlcCampaignUseCase(
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

**brand:** `typing.Optional[str]` — Brand id. This identifier is a string that always begins with the prefix `b_`, for example: `b_1234567890`.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` — Unique identifier for the campaign. This identifier is a string that always begins with the prefix `dlc_`, for example: `dlc_1234567890`.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the campaign.
    
</dd>
</dl>

<dl>
<dd>

**keywords:** `typing.Optional[UpsertDlcCampaignKeywords]` — Keyword response configuration.
    
</dd>
</dl>

<dl>
<dd>

**links:** `typing.Optional[UpsertDlcCampaignLinks]` — Legal documentation links.
    
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

**options:** `typing.Optional[UpsertDlcCampaignOptions]` — Campaign configuration options.
    
</dd>
</dl>

<dl>
<dd>

**sample_messages:** `typing.Optional[typing.Sequence[str]]` — Example messages for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**use_case:** `typing.Optional[UpsertDlcCampaignUseCase]` — Use case for the campaign.
    
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

Validate your 10DLC campaign configuration against carrier requirements and compliance rules.
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
    campaign_id="dlc_1234567890",
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

**campaign_id:** `str` 

Unique identifier for the campaign.
- When validating 10DLC campaigns, it must begin with the prefix `dlc_` (e.g., `dlc_1234567890`)
- When validating toll-free campaigns, it must begin with the prefix `tf_` (e.g., `tf_1234567890`)
- When validating RCS campaigns, it must begin with the prefix `rcs_` (e.g., `rcs_1234567890`)  
    
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
    additional_info="Please autofill missing campaign fields using my brand profile",
    campaign_id="dlc_1234567890",
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

**campaign_id:** `typing.Optional[str]` 

Unique identifier for the campaign.
- When autofilling 10DLC campaigns, it must begin with the prefix `dlc_` (e.g., `dlc_1234567890`)
- When autofilling Toll-Free campaigns, it must begin with the prefix `tf_` (e.g., `tf_1234567890`)
- When autofilling RCS campaigns, it must begin with the prefix `rcs_` (e.g., `rcs_1234567890`)
    
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
    campaign_id="tf_1234567890",
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

**campaign_id:** `str` — Unique identifier of toll-free campaign. Must begin with the prefix `tf_`.
    
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
    campaign_id="tf_1234567890",
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

**campaign_id:** `str` — Unique identifier of the toll-free campaign to submit. Must begin with the prefix `tf_`.
    
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
    brand="b_1234567890",
    campaign_id="tf_1234567890",
    monthly_volume="1,000",
    name="Pinnacle",
    opt_in=UpsertTollFreeSchemaOptIn(
        method="DIGITAL",
        url="https://www.pinnacle.sh/",
        workflow_description="Visit https://www.pinnacle.sh/",
    ),
    production_message_content="Join the Pinnacle workshop tomorrow and send your first RCS!",
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

**brand:** `typing.Optional[str]` — Brand id. This identifier is a string that always begins with the prefix `b_`, for example: `b_1234567890`.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` — Unique identifier for the campaign. This identifier is a string that always begins with the prefix `tf_`, for example: `tf_1234567890`.
    
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
    campaign_id="dlc_1234567890",
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

**campaign_id:** `str` 

Unique identifier for the campaign.
- When validating 10DLC campaigns, it must begin with the prefix `dlc_` (e.g., `dlc_1234567890`)
- When validating toll-free campaigns, it must begin with the prefix `tf_` (e.g., `tf_1234567890`)
- When validating RCS campaigns, it must begin with the prefix `rcs_` (e.g., `rcs_1234567890`)  
    
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
    additional_info="Please autofill missing campaign fields using my brand profile",
    campaign_id="dlc_1234567890",
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

**campaign_id:** `typing.Optional[str]` 

Unique identifier for the campaign.
- When autofilling 10DLC campaigns, it must begin with the prefix `dlc_` (e.g., `dlc_1234567890`)
- When autofilling Toll-Free campaigns, it must begin with the prefix `tf_` (e.g., `tf_1234567890`)
- When autofilling RCS campaigns, it must begin with the prefix `rcs_` (e.g., `rcs_1234567890`)
    
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
    campaign_id="rcs_1234567890",
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

**campaign_id:** `str` — Unique identifier of the RCS campaign. Must begin with the prefix `rcs_`.
    
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
    campaign_id="rcs_1234567890",
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

**campaign_id:** `str` — Unique identifier of the RCS campaign to retrieve. Must begin with the prefix `rcs_`.
    
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
    RcsAgentEmail,
    RcsAgentPhone,
    RcsAgentWebsite,
    UpsertRcsAgent,
    UpsertRcsLinks,
    UpsertRcsOptIn,
    UpsertRcsOptOut,
    UpsertRcsUseCase,
)

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.campaigns.rcs.upsert(
    agent=UpsertRcsAgent(
        color="#000000",
        description="Engaging campaigns with RBM – next-gen SMS marketing with rich content and better analytics.",
        emails=[
            RcsAgentEmail(
                email="founders@trypinnacle.app",
                label="Email Us",
            )
        ],
        hero_url="https://agent-logos.storage.googleapis.com/_/m0bk9mmw7kfynqiKSPfsaoc6",
        icon_url="https://agent-logos.storage.googleapis.com/_/m0bk9gvlDunZEw1krfruZmw3",
        name="Pinnacle Software Development",
        phones=[
            RcsAgentPhone(
                label="Contact us directly",
                phone="+14154467821",
            )
        ],
        websites=[
            RcsAgentWebsite(
                label="Get started with Pinnacle",
                url="https://www.trypinnacle.app/",
            )
        ],
    ),
    brand_verification_url="https://www.pinnacle.sh/articles-of-incorporation.pdf",
    brand="b_1234567890",
    campaign_id="rcs_1234567890",
    expected_agent_responses=[
        "Here are the things I can help you with.",
        "I can assist you with booking an appointment, or you may choose to book manually.",
        "Here are the available times to connect with a representative tomorrow.",
        "Your appointment has been scheduled.",
    ],
    links=UpsertRcsLinks(
        privacy_policy="https://www.trypinnacle.app/privacy",
        terms_of_service="https://www.trypinnacle.app/terms",
    ),
    opt_in=UpsertRcsOptIn(
        method="WEBSITE",
        terms_and_conditions="Would you like to subscribe to Pinnacle?",
    ),
    opt_out=UpsertRcsOptOut(
        description="Reply STOP to opt-out anytime.",
        keywords=["STOP", "UNSUBSCRIBE", "END"],
    ),
    use_case=UpsertRcsUseCase(
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

**agent:** `typing.Optional[UpsertRcsAgent]` — Create an agent for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**brand_verification_url:** `typing.Optional[str]` — Link to document verifying the brand's name. This may be the certificate of incorporation, business license, or other relevant document. You can typically find this on the Secretary of State website.
    
</dd>
</dl>

<dl>
<dd>

**brand:** `typing.Optional[str]` — Unique identifier for the brand.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` — Unique identifier for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**expected_agent_responses:** `typing.Optional[typing.Sequence[str]]` — List of what the agent might say to users (1-5 required).
    
</dd>
</dl>

<dl>
<dd>

**links:** `typing.Optional[UpsertRcsLinks]` — Legal documentation links.
    
</dd>
</dl>

<dl>
<dd>

**opt_in:** `typing.Optional[UpsertRcsOptIn]` — Opt-in configuration.
    
</dd>
</dl>

<dl>
<dd>

**opt_out:** `typing.Optional[UpsertRcsOptOut]` — Opt-out configuration.
    
</dd>
</dl>

<dl>
<dd>

**use_case:** `typing.Optional[UpsertRcsUseCase]` — Use case classification for the campaign.
    
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
    campaign_id="dlc_1234567890",
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

**campaign_id:** `str` 

Unique identifier for the campaign.
- When validating 10DLC campaigns, it must begin with the prefix `dlc_` (e.g., `dlc_1234567890`)
- When validating toll-free campaigns, it must begin with the prefix `tf_` (e.g., `tf_1234567890`)
- When validating RCS campaigns, it must begin with the prefix `rcs_` (e.g., `rcs_1234567890`)  
    
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
    text="Hey!",
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

**options:** `typing.Optional[SendSmsOptions]` — Additional settings to customize SMS delivery.
    
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
from rcs.messages.mms import SendMmsOptions

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.messages.mms.send(
    from_="+14155164736",
    media_urls=[
        "https://fastly.picsum.photos/id/941/300/300.jpg?hmac=mDxM9PWSqRDjecwSCEpzU4bj35gqnG7yA25OL29uNv0"
    ],
    options=SendMmsOptions(
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

**options:** `typing.Optional[SendMmsOptions]` — Control how your MMS is processed and delivered.
    
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
from rcs import Pinnacle, RichButton_OpenUrl, RichTextMessage

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.messages.rcs.send(
    request=RichTextMessage(
        quick_replies=[
            RichButton_OpenUrl(
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

**request:** `RichMessage` 
    
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

<details><summary><code>client.messages.rcs.<a href="src/rcs/messages/rcs/client.py">send_typing</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a typing indicator from an RCS agent to a recipient.

This endpoint allows RCS agents to display a typing indicator to recipients. The indicator is a message bubble with animated typing dots like this: <img src="https://server.trypinnacle.app/storage/v1/object/public/pinnacle-public-assets/ios-typing-indicator.png" alt="Typing Indicator" style="display: inline; height: 1.5em; vertical-align: middle; margin: 0 4px;" />

**Use Case:** Typing indicators are especially useful for providing feedback to users while the agent is thinking or generating a response that may take some time, creating a more engaging conversational experience.

**Expiration:** Typing indicators automatically expire after around 20 seconds or when the agent sends a message, whichever comes first.

**Frequency:** You can send typing indicators as many times as needed, though only one will be displayed at a time. Sending multiple typing indicators will extend the duration of the current indicator.

> **Note:** Typing indicators are best-effort hints, not delivery-guaranteed state. The platform is allowed to coalesce or drop them, and the client UI decides when to show/hide.
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
from rcs.messages.rcs import SendTypingIndicatorSchemaOptions

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.messages.rcs.send_typing(
    agent_id="agent_pinnacle",
    to="+14154746461",
    options=SendTypingIndicatorSchemaOptions(
        test_mode=False,
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

**agent_id:** `str` 

The unique identifier of the RCS agent sending the typing indicator. <br>

Format: `agent_` followed by alphanumeric characters (e.g., `agent_pinnacle`).
    
</dd>
</dl>

<dl>
<dd>

**to:** `str` 

The recipient's phone number in E.164 format. <br>

Must include country code with a leading plus sign (e.g., `+14155551234`).
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[SendTypingIndicatorSchemaOptions]` — Configure how your typing indicator is sent.
    
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
from rcs import Pinnacle, RichButton_OpenUrl, RichText

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.messages.rcs.validate(
    request=RichText(
        quick_replies=[
            RichButton_OpenUrl(
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
from rcs import AttachWebhookByIdParams, Pinnacle

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.phone_numbers.webhook.attach(
    phone="%2B14155551234",
    request=AttachWebhookByIdParams(
        webhook_id="wh_1234567890",
        event="MESSAGE.STATUS",
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

Must be a phone number that you own and have already [purchased](./buy) through the API. A phone number can have multiple webhooks attached to it.
    
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
    webhook_id="wh_1234567890",
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

**webhook_id:** `str` 

The unique identifier of the webhook you want to detach from the phone number. <br>

This must be a valid webhook ID that is currently attached to the specified phone number. This identifier is a string that always begins with the prefix `wh_`, for example: `wh_1234567890`.
    
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

Link a phone number to a specific campaign. Phone numbers must be linked to a campaign to send messages.
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
    campaign_id="tf_1234567890",
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

**campaign_id:** `str` 

Unique identifier for the campaign. <br>

 - **TOLL_FREE** campaigns:
   - Must begin with the prefix `tf_`
   - Example: `tf_1234567890`
 - **10DLC** campaigns:
   - Must begin with the prefix `dlc_`
   - Example: `dlc_1234567890`
    
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
    brand_id="b_1234567890",
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

**brand_id:** `str` — The unique identifier of the brand you want to retrieve the status for. This identifier is a string that always begins with the prefix `b_`, for example: `b_1234567890`.
    
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
    campaign_id="tf_1234567890",
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

**campaign_id:** `str` — The unique identifier of the toll-free campaign you want to retrieve the status for. This identifier is a string that always begins with the prefix `tf_`, for example: `tf_1234567890`.
    
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

Retrieve a 10DLC campaign's status.
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
    campaign_id="dlc_1234567890",
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

**campaign_id:** `str` — The unique identifier of the 10DLC campaign you want to retrieve the status for. This identifier is a string that always begins with the prefix `dlc_`, for example: `dlc_1234567890`.
    
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
    campaign_id="rcs_1234567890",
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

**campaign_id:** `str` — The unique identifier of the RCS campaign you want to retrieve the status for. This identifier is a string that always begins with the prefix `rcs_`, for example: `rcs_1234567890`.
    
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

Update the destination or expiration date of an existing shortened URL. Expiring links cannot be updated into a permalink.
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
from rcs.tools.file import DownloadOptions, UploadFileOptions

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.tools.file.upload(
    content_type="image/jpeg",
    size=1024,
    name="test.jpg",
    options=UploadFileOptions(
        delete_at="2025-12-31T23:59:59Z",
        download=DownloadOptions(
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

**options:** `typing.Optional[UploadFileOptions]` — Additional configurations for your file.
    
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

<details><summary><code>client.tools.file.<a href="src/rcs/tools/file/client.py">refresh</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Refresh expiring presigned URLs for Pinnacle-hosted files to extend their access time.

<Callout type="info">
  This only works for presigned download URLs. At this moment, you cannot refresh a presigned upload URL, generate a new one instead.
</Callout>
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
client.tools.file.refresh(
    urls=[
        "https://server.trypinnacle.app/storage/v1/object/sign/vault/3/test.jpg?token=oldtoken",
        "https://server.trypinnacle.app/storage/v1/object/sign/vault/3/document.pdf?token=oldtoken2",
        "invalid/url",
        "https://google.com",
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

**urls:** `typing.Sequence[str]` — Array of file URLs to refresh for extended access. Provided URLs must be presigned URLs (i.e. `https://server.trypinnacle.app/storage/v1/object/sign/...`). Invalid or external URLs will be returned unchanged in the response.
    
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

Retrieve contact information as a vCard and get a presigned URL to download the file. Contact cards can be sent [via MMS](/api-reference/messages/send-mms) as a media file.
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
    id="cc_1234567890",
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

**id:** `str` — The unique identifier of the contact. This identifier is a string that always begins with the prefix `cc_`, for example: `cc_1234567890`.
    
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

Create a new contact card or updates an existing one with full vCard data. Contact cards can be sent [via MMS](/api-reference/messages/send-mms) as a media file.
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
    id="cc_1234567890",
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

**id:** `typing.Optional[str]` — The unique identifier of the contact. This identifier is a string that always begins with the prefix `cc_`, for example: `cc_1234567890`.
    
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

