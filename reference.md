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

Create a new brand or update an existing one.

<Note>
**To create a new brand:** Omit `id` — one will be generated automatically.

All fields are **required** except `description` and `dba`, and will be validated when [submitted](/api-reference/brands/submit).
</Note>
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
from rcs.brands import UpsertBrandSchemaContact

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.brands.upsert(
    address="500 Folsom St, San Francisco, CA 94105",
    contact=UpsertBrandSchemaContact(
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
    entity_type="LLC",
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

**contact:** `typing.Optional[UpsertBrandSchemaContact]` — Contact information for the brand.
    
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

**sector:** `typing.Optional[UpsertBrandSchemaSector]` — Industry the brand operates in.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[UpsertBrandSchemaType]` — Legal structure of the brand.
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `typing.Optional[UpsertBrandSchemaEntityType]` — Legal entity type of the brand.
    
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

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.brands.validate()

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

**address:** `typing.Optional[str]` — Primary brand address where this brand is located.
    
</dd>
</dl>

<dl>
<dd>

**contact:** `typing.Optional[OptionalContacts]` 
    
</dd>
</dl>

<dl>
<dd>

**dba:** `typing.Optional[str]` — "Doing Business As" name - the public name this brand operates under.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Brief description of what this brand does.
    
</dd>
</dl>

<dl>
<dd>

**ein:** `typing.Optional[str]` — Employer Identification Number (EIN) assigned by the IRS.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Main contact email address for this brand.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Legal name of the brand as registered.
    
</dd>
</dl>

<dl>
<dd>

**sector:** `typing.Optional[CompanySectorEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[CompanyTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `typing.Optional[CompanyEntityTypeEnum]` — Legal entity type of the brand.
    
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

<details><summary><code>client.brands.<a href="src/rcs/brands/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all brands with optional filtering and pagination. Results are sorted by creation date, newest first.
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
client.brands.list()

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

**page_index:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListBrandsRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**is_archived:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Case-insensitive substring search on brand name.
    
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

<details><summary><code>client.audiences.<a href="src/rcs/audiences/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all audiences with optional filtering and pagination. Results are sorted by creation date, newest first.
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
client.audiences.list()

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

**page_index:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter audiences by name (partial match).
    
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

<details><summary><code>client.contacts.<a href="src/rcs/contacts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all contacts with optional filtering and pagination. Results are sorted by creation date, newest first.
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
client.contacts.list()

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

**page_index:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — Filter contacts by phone number (E.164 format).
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter contacts by name (partial match).
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — Filter contacts by tags.
    
</dd>
</dl>

<dl>
<dd>

**is_archived:** `typing.Optional[bool]` — Filter contacts by archived status.
    
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

**sort_order:** `typing.Optional[ConversationsListMessagesRequestSortOrder]` 

Sort order for messages. <br>

- `asc`: Oldest messages first
- `desc`: Newest messages first (default)
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[ConversationsListMessagesRequestDirection]` 

Filter messages by direction. <br>

- `INBOUND`: Messages received from contacts
- `OUTBOUND`: Messages sent to contacts
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ConversationsListMessagesRequestStatus]` — Filter messages by delivery status.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ConversationsListMessagesRequestType]` — Filter messages by protocol type.
    
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

<details><summary><code>client.messages.<a href="src/rcs/messages/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all messages with optional filtering and pagination. Results are sorted by creation date, newest first.
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
client.messages.list()

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

**page_index:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[ListMessagesRequestDirection]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListMessagesRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ListMessagesRequestType]` 
    
</dd>
</dl>

<dl>
<dd>

**method:** `typing.Optional[ListMessagesRequestMethod]` — Filter by the method used to send the message.
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Filter by sender phone number (E.164 format) or agent id.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[str]` — Filter by recipient phone number (E.164 format).
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — Search message content (partial match, case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**date_from:** `typing.Optional[dt.datetime]` — Filter messages created on or after this date (ISO 8601 format).
    
</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[dt.datetime]` — Filter messages created on or before this date (ISO 8601 format).
    
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

<details><summary><code>client.phone_numbers.<a href="src/rcs/phone_numbers/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all owned phone numbers with pagination. Results are sorted by creation date, newest first.
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
client.phone_numbers.list()

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

**page_index:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
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

## Rcs
<details><summary><code>client.rcs.<a href="src/rcs/rcs/client.py">get_agent</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of an RCS agent by its ID.

Returns the agent's configuration including display name, description, logo, hero image,
contact information, and other settings.
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
client.rcs.get_agent(
    agent_id="agent_abc123def456",
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

**agent_id:** `str` — The RCS agent ID (must be prefixed with `agent_`).
    
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

**phone_numbers:** `typing.Sequence[str]` 

List of phone numbers to check RCS capabilities for (E.164 format). <br><br>
**Limit:** 1 min
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Optional RCS agent ID (prefixed with 'agent_') to check capabilities of a number from a specific agent.
    
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

**identifiers:** `typing.Sequence[str]` 

List of URLs or phone numbers in E.164 format that the webhook is attached to. <br><br>
**Limit:** 1 min
    
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

<details><summary><code>client.webhooks.<a href="src/rcs/webhooks/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all webhooks with optional filtering and pagination. Results are sorted by creation date, newest first.
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
client.webhooks.list()

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

**page_index:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListWebhooksRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint:** `typing.Optional[str]` — Filter webhooks by endpoint URL (partial match, case-insensitive).
    
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

<details><summary><code>client.webhooks.<a href="src/rcs/webhooks/client.py">attach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach a webhook to one or more senders (phone numbers or RCS agent IDs) to receive real-time event notifications. <br>

You can attach an existing webhook by providing its ID, or create a new webhook by specifying a name and URL. Supports bulk operations with up to 50 senders per request. <br>

Subscriptions are additive — attaching new senders does not remove existing ones. Re-attaching the same sender updates the event type filter without creating duplicates. <br>

**Custom headers** may be provided in either case via the optional `headers` field. When attaching a new webhook, the headers are stored on the webhook and sent on every delivery. When attaching an existing `webhookId`, supplying `headers` **overwrites** the stored headers on that webhook — omit the field to leave them unchanged, or pass an empty object `{}` to clear them. The reserved `PINNACLE-SIGNING-SECRET` header is always set by Pinnacle and cannot be overridden.
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
client.webhooks.attach(
    senders=["+14155551234", "agent_abc123"],
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

**senders:** `typing.Sequence[str]` — Array of senders to attach the webhook to. Can be phone numbers in E.164 format or RCS agent IDs.
    
</dd>
</dl>

<dl>
<dd>

**webhook_id:** `typing.Optional[str]` 

Existing webhook ID (starts with `wh_`). Provide this OR `name` + `url` to create a new webhook. The webhook must be in ENABLED status. Disabled webhooks can be re-enabled from the [dashboard](https://app.pinnacle.sh/dashboard/development/webhooks).

Supplying `headers` alongside `webhookId` **overwrites** the stored headers on the webhook. Omit `headers` to leave them unchanged.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name for a new webhook (required if no `webhookId`).
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — HTTPS endpoint URL for a new webhook (required if no `webhookId`).
    
</dd>
</dl>

<dl>
<dd>

**event:** `typing.Optional[WebhookEventEnum]` 

Event type filter for the subscription. Set to `null` to receive all events. <br>

`USER.TYPING` is only supported for RCS agent senders, not phone numbers.
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 

Optional custom HTTP headers (key-value map) to include when dispatching webhook events to the endpoint.

Header names must start with a letter or digit and contain only letters, digits, `-`, or `_` (matching the pattern `^[A-Za-z0-9][A-Za-z0-9_-]*$`). Names are case-insensitive per [RFC 9110](https://datatracker.ietf.org/doc/html/rfc9110#name-field-names) and are normalized to uppercase before storage and sending.

When provided with an existing `webhookId`, these headers **overwrite** any headers currently stored on that webhook. Omit to leave existing headers unchanged.

The reserved `PINNACLE-SIGNING-SECRET` header is silently ignored and cannot be overridden.
    
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

<details><summary><code>client.webhooks.<a href="src/rcs/webhooks/client.py">detach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach a webhook from one or more senders (phone numbers or RCS agent IDs) to stop receiving event notifications. <br>

The webhook itself is not deleted and remains available for use with other senders. Works regardless of webhook status. Supports bulk operations with up to 50 senders per request.
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
client.webhooks.detach(
    webhook_id="webhookId",
    senders=["+14155551234", "agent_abc123"],
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

**webhook_id:** `str` — Webhook ID to detach (starts with `wh_`). Must be a webhook owned by your team.
    
</dd>
</dl>

<dl>
<dd>

**senders:** `typing.Sequence[str]` — Array of senders to detach the webhook from. Can be phone numbers in E.164 format or RCS agent IDs.
    
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

**contacts:** `typing.Sequence[str]` 

Array of phone numbers (E.164 format) or contact IDs. <br><br>
**Limit:** 1 min
    
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

**contacts:** `typing.Sequence[str]` 

Array of phone numbers (E.164 format) or contact IDs. <br><br>
**Limit:** 1 min
    
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

Create a new 10DLC campaign or update an existing one.

<Note>
**To create a new campaign:** Omit `campaignId` — one will be generated automatically.

**Before you start:** Create a [brand](/api-reference/brands/upsert) first — you'll need its `id` for the [`brand`](#request.body.brand) field.

All fields are **required** unless specified otherwise, and will be validated when [submitted](/api-reference/campaigns/10-dlc/submit).

**See the response for example values for each field.**
</Note>
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
    DlcCampaignHelpKeywords,
    DlcCampaignKeywords,
    DlcCampaignLinks,
    DlcCampaignOptInKeywords,
    DlcCampaignOptions,
    DlcCampaignOptOutKeywords,
    DlcCampaignUseCase,
)

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.campaigns.dlc.upsert(
    auto_renew=True,
    brand="b_1234567890",
    description="This campaign sends transactional SMS messages to customers who have opted in, including account notifications, security alerts, and customer care responses. Messages are sent when triggered by account activity such as login attempts, password changes, order updates, or support inquiries. All messages include required STOP/HELP disclosures and comply with TCPA guidelines.",
    keywords=DlcCampaignKeywords(
        help=DlcCampaignHelpKeywords(
            message="Pinnacle Software Development Inc.: For assistance, visit https://pinnacle.sh/support or email founders@trypinnacle.app. Msg&data rates may apply. Reply STOP to cancel.",
            values=["HELP", "SUPPORT", "INFO"],
        ),
        opt_in=DlcCampaignOptInKeywords(
            message="Pinnacle Software Development Inc.: You're enrolled in account & security alerts. Msg&data rates may apply. Message frequency varies. Reply HELP for help, STOP to cancel. Terms: https://pinnacle.sh/terms Privacy: https://pinnacle.sh/privacy",
            values=["START", "YES", "SUBSCRIBE"],
        ),
        opt_out=DlcCampaignOptOutKeywords(
            message="Pinnacle Software Development Inc.: You're unsubscribed and will receive no further texts. For assistance, visit https://pinnacle.sh or call 877-389-0460. Reply START to resubscribe.",
            values=["STOP", "CANCEL", "UNSUBSCRIBE"],
        ),
    ),
    links=DlcCampaignLinks(
        privacy_policy="https://www.pinnacle.sh/privacy",
        terms_of_service="https://www.pinnacle.sh/terms",
    ),
    message_flow='The user fills out a paper form during onboarding at [Address] which they learn about at our website (https://pinnacle.sh) in which they provide their phone number and sign their consent. The form includes a disclaimer: "By signing this form and providing your phone number, you agree to receive SMS Mixed - Account Notification, Customer Care, Security Alert, Delivery Notification from Pinnacle Software Development Inc. Message frequency may vary. Standard Message and Data Rates may apply. Reply STOP to opt out. Reply HELP for help. Consent is not a condition of purchase. Your mobile information will not be sold or shared with third parties for promotional or marketing purposes." Once the information is entered into the system, the user receives a confirmation SMS: "Thank you for signing up for SMS updates from Pinnacle Software Development Inc. Msg freq may vary. Std msg & data rates apply. Reply STOP to opt out, HELP for help." Link to paper form: https://www.pinnacle.sh/opt-in',
    name="Pinnacle's Account Notifications",
    options=DlcCampaignOptions(
        affiliate_marketing=False,
        age_gated=False,
        direct_lending=False,
        embedded_link="https://www.pinnacle.sh/example",
        embedded_phone=False,
        number_pooling=False,
    ),
    sample_messages=[
        "Pinnacle Software Development Inc.: We're here to help. Visit https://pinnacle.sh or call 877-389-0460. Msg&data rates may apply. Reply STOP to cancel.",
        "Pinnacle Software Development Inc.: You're enrolled in account & security alerts. Msg&data rates may apply. Message frequency varies. Reply HELP for help, STOP to cancel. Terms: https://pinnacle.sh/terms/ Privacy: https://pinnacle.sh/privacy/",
        "Pinnacle Software Development Inc.: An update has been made to your account. Read it in the portal.",
        "Pinnacle Software Development Inc.: We received your message. A team member will reply shortly. For immediate help call 877-389-0460. Msg&data rates may apply. Reply STOP to cancel.",
    ],
    use_case=DlcCampaignUseCase(
        sub=["ACCOUNT_NOTIFICATION", "CUSTOMER_CARE", "SECURITY_ALERT"],
        value="MIXED",
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

**description:** `typing.Optional[str]` 

Description of the campaign. Explain the purpose, use case, and types of messages your campaign will send.

**Example:** `This campaign allows users who have specifically opted in to interact with our chatbot for a range of automated services, including order status notifications, shipping updates, security alerts, and help desk support. Users can manage their account, receive transactional SMS prompts, and access interactive support. They may also share images, such as receipts, and receive immediate responses for support or account updates. All messages are strictly transactional or support-related, never unsolicited, and initiated only after clear user consent.`
    
</dd>
</dl>

<dl>
<dd>

**keywords:** `typing.Optional[DlcCampaignKeywords]` — Keyword response configuration.
    
</dd>
</dl>

<dl>
<dd>

**links:** `typing.Optional[DlcCampaignLinks]` — Legal documentation links.
    
</dd>
</dl>

<dl>
<dd>

**message_flow:** `typing.Optional[str]` — Describe your opt-in workflow. See the [Opt-In Methods and Workflow](/guides/campaigns/opt-in-compliance#opt-in-methods-and-workflow) section for requirements and examples.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Display name of the campaign.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[DlcCampaignOptions]` — Campaign configuration options.
    
</dd>
</dl>

<dl>
<dd>

**sample_messages:** `typing.Optional[typing.Sequence[str]]` — Example messages for the campaign. Include 1-5 messages that represent the types of messages you will send. See the [Sample Messages](/guides/campaigns/opt-in-compliance#sample-messages) section for requirements and examples.
    
</dd>
</dl>

<dl>
<dd>

**use_case:** `typing.Optional[DlcCampaignUseCase]` — Use case for the campaign.
    
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

<details><summary><code>client.campaigns.dlc.<a href="src/rcs/campaigns/dlc/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all 10DLC campaigns with optional filtering and pagination. Results are sorted by creation date, newest first.
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
client.campaigns.dlc.list()

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

**page_index:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListDlcCampaignsRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**brand_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter by campaign name (partial match, case-insensitive).
    
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

Create a new toll-free campaign or update an existing one.

<Note>
**To create a new campaign:** Omit `campaignId` — one will be generated automatically.

**Before you start:** Create a [brand](/api-reference/brands/upsert) first — you'll need its `id` for the [`brand`](#request.body.brand) field.

All fields are **required** unless specified otherwise, and will be validated when [submitted](/api-reference/campaigns/toll-free/submit).

**See the response for example values for each field.**
</Note>
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
    TollFreeCampaignHelpKeywords,
    TollFreeCampaignKeywords,
    TollFreeCampaignLinks,
    TollFreeCampaignOptIn,
    TollFreeCampaignOptInKeywords,
    TollFreeCampaignOptions,
    TollFreeCampaignUseCase,
)

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.campaigns.toll_free.upsert(
    brand="b_1234567890",
    campaign_id="tf_1234567890",
    keywords=TollFreeCampaignKeywords(
        help=TollFreeCampaignHelpKeywords(
            message="Pinnacle Software Development Inc.: For assistance, visit https://pinnacle.sh/support or email founders@trypinnacle.app. Msg&data rates may apply. Reply STOP to cancel.",
        ),
        opt_in=TollFreeCampaignOptInKeywords(
            message="Pinnacle Software Development Inc.: You're enrolled in account & security alerts. Msg&data rates may apply. Message frequency varies. Reply HELP for help, STOP to cancel. Terms: https://pinnacle.sh/terms/ Privacy: https://pinnacle.sh/privacy/",
            keywords=["START", "SUBSCRIBE"],
        ),
    ),
    links=TollFreeCampaignLinks(
        privacy_policy="https://www.pinnacle.sh/privacy",
        terms_of_service="https://www.pinnacle.sh/terms",
    ),
    monthly_volume="10,000",
    name="Pinnacle",
    opt_in=TollFreeCampaignOptIn(
        method="PAPER",
        url="https://www.pinnacle.sh/opt-in",
        workflow_description="End users opt-in when filling out the in-person intake forms where they will write their phone numbers and check a box indicating that they've opted in to messages. Link to paper form: https://www.pinnacle.sh/opt-in",
    ),
    options=TollFreeCampaignOptions(
        age_gated=False,
    ),
    production_message_content="Hi [First Name], your order #[Order ID] has shipped and will arrive [Date]. Track here: [URL]. Reply HELP for help or STOP to unsubscribe.",
    use_case=TollFreeCampaignUseCase(
        summary="Customers who have opted into text messages can interact with our automated SMS chatbot to receive transaction-driven notifications (order status, shipping updates, account alerts), ask support questions, share photos with friends, and manage their account details via simple, conversational text flows. All messages are transactional or interactive flows customers opt into. Users can send images (e.g., receipts) and get guided replies.",
        value="CHATBOT",
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

**keywords:** `typing.Optional[TollFreeCampaignKeywords]` — Keyword response configuration.
    
</dd>
</dl>

<dl>
<dd>

**links:** `typing.Optional[TollFreeCampaignLinks]` — Legal documentation links.
    
</dd>
</dl>

<dl>
<dd>

**monthly_volume:** `typing.Optional[MessageVolumeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Display name of the campaign. This is not sent to carriers for approval and is only used for your reference on the Pinnacle dashboard.
    
</dd>
</dl>

<dl>
<dd>

**opt_in:** `typing.Optional[TollFreeCampaignOptIn]` — Opt-in method and workflow.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[TollFreeCampaignOptions]` — Campaign configuration options.
    
</dd>
</dl>

<dl>
<dd>

**production_message_content:** `typing.Optional[str]` — Example message(s) that would be sent in production. Should reflect the actual content users will receive, including HELP/STOP disclosures. See the [Production Message Content](/guides/campaigns/opt-in-compliance#production-message-content) section for requirements.
    
</dd>
</dl>

<dl>
<dd>

**use_case:** `typing.Optional[TollFreeCampaignUseCase]` — Use case classification for the campaign.
    
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

<details><summary><code>client.campaigns.toll_free.<a href="src/rcs/campaigns/toll_free/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all toll-free campaigns with optional filtering and pagination. Results are sorted by creation date, newest first.
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
client.campaigns.toll_free.list()

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

**page_index:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListTollFreeCampaignsRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**brand_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter by campaign name (partial match, case-insensitive).
    
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

Create a new RCS campaign or update an existing one.

<Note>
**To create a new campaign:** Omit `campaignId` — one will be generated automatically.

**Before you start:** Create a [brand](/api-reference/brands/upsert) first — you'll need its `id` for the [`brand`](#request.body.brand) field.

All fields are **required** unless specified otherwise, and will be validated when [submitted](/api-reference/campaigns/rcs/submit).
</Note>
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
    RcsAgent,
    RcsAgentEmail,
    RcsAgentPhone,
    RcsAgentWebsite,
    RcsCampaignHelpKeywords,
    RcsCampaignKeywords,
    RcsCampaignOptInKeywords,
    RcsCampaignOptOutKeywords,
    RcsCampaignTraffic,
    RcsLinks,
)

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.campaigns.rcs.upsert(
    agent=RcsAgent(
        color="#000000",
        description="Experience the power of RCS messaging with interactive demos. Test rich features like carousels, suggested replies, and media sharing. Get started with our developer-friendly APIs.",
        emails=[
            RcsAgentEmail(
                email="founders@trypinnacle.app",
                label="Email Us",
            )
        ],
        hero_url="https://pncl.to/D6pDSqGxqgfbCfQmw4gXdnlHu4uSB4",
        icon_url="https://pncl.to/mq_tdIDenRb5eYpJiM8-3THCaUBrZP",
        name="Pinnacle - RCS Demo",
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
    brand="b_1234567890",
    campaign_id="rcs_1234567890",
    expected_agent_responses=[
        "Here are the things I can help you with.",
        "I can assist you with booking an appointment, or you may choose to book manually.",
        "Here are the available times to connect with a representative tomorrow.",
        "Your appointment has been scheduled.",
    ],
    links=RcsLinks(
        privacy_policy="“https://www.trypinnacle.app/privacy”",
        terms_of_service="“https://www.trypinnacle.app/terms”",
    ),
    use_case_description="Pinnacle is a developer-focused RCS assistant that helps teams design, test, and optimize rich messaging experiences across SMS, MMS, and RCS. The agent acts as both an “onboarding guide” for new customers and a “best-practices coach” for existing teams exploring higher-value RCS workflows like rich cards, carousels, and suggested actions.<br>\nThe agent delivers a mix of operational updates and educational content (2–6 messages/month). Content includes important platform notices (e.g., deliverability or throughput changes), implementation tips with sample RCS templates, and personalized recommendations on how to upgrade existing SMS campaigns into richer, higher-converting RCS conversations.\n",
    messaging_type="OTP",
    cta_media="“https://www.pinnacle.sh/send”",
    opt_in_method="We ensure consent through an explicit opt-in process that follows 10DLC best practices.Users must agree to receive messages from Pinnacle before the agent sends them any messages.<br>\nUsers agree to these messages by signing an opt-in paper form that they can be found online at https://www.pinnacle.sh/opt-in. We only send messages once users have filled out the form and submitted it to us via email or through the dashboard.\n",
    keywords=RcsCampaignKeywords(
        help=RcsCampaignHelpKeywords(
            message="Email founders@trypinnacle.app for support.",
            keywords=["HELP", "SUPPORT"],
        ),
        opt_in=RcsCampaignOptInKeywords(
            message="Welcome back to Pinnacle!<br>\n🔔 You're now subscribed to Pinnacle - RCS Demo and will continue receiving important updates and news. Feel free to contact this us at any time for help.<br>\n\nReply STOP to opt out and HELP for support. Message & rates may apply.\n",
            keywords=["START", "SUBSCRIBE"],
        ),
        opt_out=RcsCampaignOptOutKeywords(
            message="You've been unsubscribed from Pinnacle - RCS Demo and will no longer receive notifications. If you ever change your mind, reply START or SUBSCRIBE to rejoin anytime.",
            keywords=["STOP", "UNSUBSCRIBE", "END"],
        ),
    ),
    traffic=RcsCampaignTraffic(
        monthly_website=10000,
        monthly_rcs_estimate=10000,
    ),
    cta_language="By checking this box and submitting this form, you consent to receive transactional text messages for support, appointment, and reminder messages from Pinnacle Software Development Inc. Reply STOP to opt out. Reply HELP for help. Standard message and data rates may apply. Message frequency may vary. View our Terms and Conditions at https://www.pinnacle.sh/terms. View our Privacy Policy at https://www.pinnacle.sh/privacy.",
    demo_trigger='Text "START" to trigger the flow.',
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

**agent:** `typing.Optional[RcsAgent]` — Create an agent for the campaign.
    
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

**expected_agent_responses:** `typing.Optional[typing.Sequence[str]]` 

List of what the agent might say to users. See the [Expected Agent Responses](/guides/campaigns/rcs-compliance#expected-agent-responses) section for requirements. <br><br>
**Limit:** 1 to 5
    
</dd>
</dl>

<dl>
<dd>

**links:** `typing.Optional[RcsLinks]` — Legal documentation links.
    
</dd>
</dl>

<dl>
<dd>

**use_case_description:** `typing.Optional[str]` — Detailed summary of what the brand is and how this agent will be used. See the [Use Case Behavior](/guides/campaigns/rcs-compliance#use-case-behavior) section for requirements.
    
</dd>
</dl>

<dl>
<dd>

**messaging_type:** `typing.Optional[RcsMessagingTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**cta_media:** `typing.Optional[str]` — URL to the opt-in form or a URL to a screenshot of the opt-in CTA.
    
</dd>
</dl>

<dl>
<dd>

**opt_in_method:** `typing.Optional[str]` — Details on how opt-in is acquired. If it is done through a website or app, provide the link. See the [Opt-In Method](/guides/campaigns/rcs-compliance#opt-in-method) section for requirements.
    
</dd>
</dl>

<dl>
<dd>

**keywords:** `typing.Optional[RcsCampaignKeywords]` 
    
</dd>
</dl>

<dl>
<dd>

**traffic:** `typing.Optional[RcsCampaignTraffic]` 
    
</dd>
</dl>

<dl>
<dd>

**cta_language:** `typing.Optional[str]` — Required text that appears next to the opt-in checkbox for your opt-in form. This checkbox has to be unchecked by default. See the [CTA Language](/guides/campaigns/rcs-compliance#cta-language-opt-in-disclosure) section for requirements.
    
</dd>
</dl>

<dl>
<dd>

**demo_trigger:** `typing.Optional[str]` — Instructions on how an external reviewer can trigger messages and an example flow from the agent. This is usually an inbound text message to the agent that will start a flow of messages between the agent and the user. See the [Demo Trigger](/guides/campaigns/rcs-compliance#demo-trigger) section for requirements.
    
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

<details><summary><code>client.campaigns.rcs.<a href="src/rcs/campaigns/rcs/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all RCS campaigns with optional filtering and pagination. Results are sorted by creation date, newest first.
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
client.campaigns.rcs.list()

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

**page_index:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListRcsCampaignsRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**brand_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter by campaign name (partial match, case-insensitive).
    
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
from rcs import Pinnacle, RichTextMessage

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.messages.rcs.send(
    request=RichTextMessage(
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

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.messages.rcs.send_typing(
    agent_id="agent_pinnacle",
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
from rcs import Pinnacle, RichText

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.messages.rcs.validate(
    request=RichText(
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

## Messages Blast
<details><summary><code>client.messages.blast.<a href="src/rcs/messages/blast/client.py">sms</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send an SMS message to all contacts in an audience. <br>

Messages are distributed evenly across the provided sender phone numbers. <br>

Use the optional `schedule` parameter in `options` to schedule the blast for future delivery. When scheduled, the response will contain a `scheduleId` instead of blast details.
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
from rcs import Pinnacle, SmsContent

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.messages.blast.sms(
    audience_id="aud_abc123",
    senders=["+14155164736", "+14155164737"],
    message=SmsContent(
        text="Hello from Pinnacle!",
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

**audience_id:** `str` 

The audience ID to send the blast to. This identifier is a string that always begins with the prefix `aud_`, for example: `aud_abc123`. <br>

You can create an audience via [the dashboard](https://app.pinnacle.sh/dashboard/audiences) or [API](/api-reference/audiences/create).
    
</dd>
</dl>

<dl>
<dd>

**senders:** `typing.Sequence[str]` 

Array of phone numbers to send from in E.164 format. <br>

Messages will be distributed evenly across these senders.

> **Note:** Sandbox numbers cannot be used for blasts.

**Limit:** 1 min
    
</dd>
</dl>

<dl>
<dd>

**message:** `SmsContent` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[BlastSmsOptions]` — Additional settings to customize SMS blast delivery.
    
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

<details><summary><code>client.messages.blast.<a href="src/rcs/messages/blast/client.py">mms</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send an MMS message to all contacts in an audience. <br>

Messages are distributed evenly across the provided sender phone numbers. <br>

Use the optional `schedule` parameter in `options` to schedule the blast for future delivery. When scheduled, the response will contain a `scheduleId` instead of blast details.
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
from rcs import MmsContent, Pinnacle
from rcs.messages.blast import BlastMmsOptions

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.messages.blast.mms(
    audience_id="aud_abc123",
    senders=["+14155164736", "+14155164737"],
    message=MmsContent(
        media_urls=["https://fastly.picsum.photos/id/941/300/300.jpg"],
        text="Check out this image!",
    ),
    options=BlastMmsOptions(
        validate=True,
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

**audience_id:** `str` 

The audience ID to send the blast to. This identifier is a string that always begins with the prefix `aud_`, for example: `aud_abc123`. <br>

You can create an audience via [the dashboard](https://app.pinnacle.sh/dashboard/audiences) or [API](/api-reference/audiences/create).
    
</dd>
</dl>

<dl>
<dd>

**senders:** `typing.Sequence[str]` 

Array of phone numbers to send from in E.164 format. <br>

Messages will be distributed evenly across these senders.

> **Note:** Sandbox numbers cannot be used for blasts.

**Limit:** 1 min
    
</dd>
</dl>

<dl>
<dd>

**message:** `MmsContent` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[BlastMmsOptions]` — Additional settings to customize MMS blast delivery.
    
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

<details><summary><code>client.messages.blast.<a href="src/rcs/messages/blast/client.py">rcs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send an RCS message to all contacts in an audience. <br>

Messages are distributed evenly across the provided RCS agents for load balancing. Requires active RCS agents and recipient devices that support RCS Business Messaging. <br>

Use the optional `schedule` parameter in `options` to schedule the blast for future delivery. When scheduled, the response will contain a `scheduleId` instead of blast details.
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
from rcs import FallbackMessage, Pinnacle, RichButton_Trigger, RichText
from rcs.messages.blast import BlastRcsOptions

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.messages.blast.rcs(
    audience_id="aud_abc123",
    senders=["agent_pinnacle", "agent_pinnacle2"],
    message=RichText(
        quick_replies=[
            RichButton_Trigger(
                payload="payload",
                title="title",
            )
        ],
        text="Hello from Pinnacle RCS!",
    ),
    fallback=FallbackMessage(
        from_="+14155164736",
        text="Hello from Pinnacle! Reply LEARN to learn more.",
    ),
    options=BlastRcsOptions(
        transcode=True,
        validate=True,
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

**audience_id:** `str` 

The audience ID to send the blast to. This identifier is a string that always begins with the prefix `aud_`, for example: `aud_abc123`. <br>

You can create an audience via [the dashboard](https://app.pinnacle.sh/dashboard/audiences) or [API](/api-reference/audiences/create).
    
</dd>
</dl>

<dl>
<dd>

**senders:** `typing.Sequence[str]` 

Array of RCS agent IDs to send from. Each must be prefixed with `agent_`. <br>

Messages will be evenly distributed across these agents.

**Limit:** 1 min
    
</dd>
</dl>

<dl>
<dd>

**message:** `RcsValidateContent` 
    
</dd>
</dl>

<dl>
<dd>

**fallback:** `typing.Optional[FallbackMessage]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[BlastRcsOptions]` — Configure how your RCS blast is sent and tracked.
    
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

## Messages Schedule
<details><summary><code>client.messages.schedule.<a href="src/rcs/messages/schedule/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a scheduled message or blast. <br>

Works for both individual scheduled messages and scheduled blasts. Use the `scheduleId` returned when the message or blast was scheduled.
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
client.messages.schedule.cancel(
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

## Messages Schedules
<details><summary><code>client.messages.schedules.<a href="src/rcs/messages/schedules/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all scheduled messages with optional filtering and pagination. Results are sorted by creation date, newest first.
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
client.messages.schedules.list()

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

**page_index:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListScheduledMessagesRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule_type:** `typing.Optional[ListScheduledMessagesRequestScheduleType]` — Filter by schedule type — "MESSAGE" for individual messages, "BLAST" for bulk sends.
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — Search scheduled message content (partial match, case-insensitive).
    
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

## Messages Blasts
<details><summary><code>client.messages.blasts.<a href="src/rcs/messages/blasts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all blasts with optional filtering and pagination. Results are sorted by creation date, newest first.
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
client.messages.blasts.list()

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

**page_index:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**audience_id:** `typing.Optional[str]` — Filter blasts by audience ID.
    
</dd>
</dl>

<dl>
<dd>

**sender:** `typing.Optional[str]` — Filter blasts that include this sender (phone number or agent ID).
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — Search blast content (partial match, case-insensitive).
    
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

## Messages Simulate
<details><summary><code>client.messages.simulate.<a href="src/rcs/messages/simulate/client.py">user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Simulate inbound messages and button presses from a user.
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
    SimulateUserButton,
    UserButtonPress_RequestUserLocation,
)

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.messages.simulate.user(
    request=SimulateUserButton(
        from_="+14155551234",
        to="agent_abc123",
        button=UserButtonPress_RequestUserLocation(
            title="Share Location",
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

**request:** `SimulateUserParams` 
    
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

**phones:** `typing.Sequence[str]` 

List of phone number (E.164 format). <br><br>
**Limit:** 1 to 10
    
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

**phones:** `typing.Sequence[str]` 

List of phone numbers (E.164 format). <br><br>
**Limit:** 1 to 10
    
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

## Rcs Agents
<details><summary><code>client.rcs.agents.<a href="src/rcs/rcs/agents/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all RCS agents with pagination. Results are sorted by creation date, newest first.
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
client.rcs.agents.list()

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

**page_index:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**agent_type:** `typing.Optional[ListAgentsRequestAgentType]` — Filter by agent type.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Case-insensitive substring search on agent name.
    
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

## Rcs WhitelistedNumbers
<details><summary><code>client.rcs.whitelisted_numbers.<a href="src/rcs/rcs/whitelisted_numbers/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all whitelisted test numbers with optional filtering and pagination. Results are sorted by creation date, newest first.
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
client.rcs.whitelisted_numbers.list()

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

**page_index:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Filter whitelisted numbers by agent ID (prefixed with 'agent_').
    
</dd>
</dl>

<dl>
<dd>

**number:** `typing.Optional[str]` — Filter by phone number in E.164 format.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListTestNumbersRequestStatus]` — Filter by whitelist status.
    
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

## Rcs Test
<details><summary><code>client.rcs.test.<a href="src/rcs/rcs/test/client.py">create_agent</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new RCS test agent for development and testing.

## Overview

Test agents let you build and test full RCS functionality — rich cards, carousels, buttons,
quick replies, and media messages — without going through the full carrier review process.
Messages from test agents can only be sent to [whitelisted phone numbers](/api-reference/rcs-agents/test/whitelist-number).

## Limits

- **Maximum 5 test agents per account.**

## Image Requirements

| Image | Format | Max Size |
|-------|--------|----------|
| Logo  | JPEG, PNG | 50 KB |
| Hero  | JPEG, PNG | 200 KB |

## After Creation

Once your test agent is created, you'll need to:

1. **Whitelist test phone numbers** using [`POST /rcs/test/agents/{agentId}/whitelist`](/api-reference/rcs-agents/test/whitelist-number).
2. **Accept the tester invite** on each whitelisted device.
3. **Send messages** using [`POST /messages/send/rcs`](/api-reference/messages/send-rcs) with the returned agent ID as the `from` field.

> **2-Minute Cooldown**
>
> After creating a test agent, there is a mandatory 2-minute cooldown before you can whitelist phone numbers.
> This is a requirement imposed by Google's RBM platform.
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
from rcs import AgentEmailEntry, AgentPhoneEntry, AgentWebsiteEntry, Pinnacle

client = Pinnacle(
    api_key="YOUR_API_KEY",
)
client.rcs.test.create_agent(
    display_name="Acme Support",
    description="Get help with your Acme orders and account",
    logo_url="https://example.com/logo.png",
    hero_url="https://example.com/hero.png",
    phone_numbers=[
        AgentPhoneEntry(
            number="+14155550123",
            label="Support",
        )
    ],
    emails=[
        AgentEmailEntry(
            address="support@example.com",
            label="Support",
        )
    ],
    websites=[
        AgentWebsiteEntry(
            url="https://example.com",
            label="Website",
        )
    ],
    privacy_url="https://example.com/privacy",
    terms_url="https://example.com/terms",
    color="#FF6B00",
    is_conversational=True,
    agent_use_case="MULTI_USE",
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

**display_name:** `str` 

Display name of the agent shown to users in RCS conversations.
Must be between 1 and 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` 

Short description of what the agent does. Shown to users in the agent's profile.
Must be between 1 and 100 characters.
    
</dd>
</dl>

<dl>
<dd>

**logo_url:** `str` 

URL to the agent's logo image. Displayed as the agent's avatar in conversations.

**Requirements:**
- Format: JPEG or PNG
- Max file size: 50 KB
- Recommended: Square aspect ratio
    
</dd>
</dl>

<dl>
<dd>

**hero_url:** `str` 

URL to the agent's hero banner image. Displayed at the top of the agent's profile.

**Requirements:**
- Format: JPEG or PNG
- Max file size: 200 KB
- Recommended: Landscape aspect ratio
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Sequence[AgentPhoneEntry]` 

Contact phone numbers displayed on the agent's profile.
At least 1 and up to 3 entries.
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Sequence[AgentEmailEntry]` 

Contact email addresses displayed on the agent's profile.
At least 1 and up to 3 entries.
    
</dd>
</dl>

<dl>
<dd>

**websites:** `typing.Sequence[AgentWebsiteEntry]` 

Website links displayed on the agent's profile.
At least 1 and up to 3 entries.
    
</dd>
</dl>

<dl>
<dd>

**privacy_url:** `str` — URL to the agent's privacy policy.
    
</dd>
</dl>

<dl>
<dd>

**terms_url:** `str` — URL to the agent's terms and conditions.
    
</dd>
</dl>

<dl>
<dd>

**color:** `str` 

The agent's brand color as a hex color code. Used for UI accents in the RCS conversation.
Must have sufficient contrast with white for accessibility.
    
</dd>
</dl>

<dl>
<dd>

**is_conversational:** `bool` 

Whether the agent supports two-way conversations. Set to `true` if the agent
will respond to user messages. Set to `false` for send-only agents (e.g., notifications).
    
</dd>
</dl>

<dl>
<dd>

**agent_use_case:** `typing.Optional[AgentUseCase]` 
    
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

<details><summary><code>client.rcs.test.<a href="src/rcs/rcs/test/client.py">update_agent</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing RCS test agent's configuration.

All fields are optional — only include the fields you want to update.

## Image Requirements

If updating images, the same requirements apply as when creating an agent:

| Image | Format | Max Size |
|-------|--------|----------|
| Logo  | JPEG, PNG | 50 KB |
| Hero  | JPEG, PNG | 200 KB |

> **2-Minute Cooldown**
>
> After updating a test agent, there is a mandatory 2-minute cooldown before you can whitelist phone numbers.
> This is a requirement imposed by Google's RBM platform.
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
client.rcs.test.update_agent(
    agent_id="agent_abc123def456",
    display_name="Acme Premium Support",
    description="Premium support for Acme customers",
    color="#0066FF",
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

**agent_id:** `str` — The RCS agent ID (must be prefixed with `agent_`).
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` 

Display name of the agent shown to users in RCS conversations.
Must be between 1 and 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 

Short description of what the agent does.
Must be between 1 and 100 characters.
    
</dd>
</dl>

<dl>
<dd>

**logo_url:** `typing.Optional[str]` 

URL to the agent's logo image.

**Requirements:**
- Format: JPEG or PNG
- Max file size: 50 KB
- Recommended: Square aspect ratio
    
</dd>
</dl>

<dl>
<dd>

**hero_url:** `typing.Optional[str]` 

URL to the agent's hero banner image.

**Requirements:**
- Format: JPEG or PNG
- Max file size: 200 KB
- Recommended: Landscape aspect ratio
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[AgentPhoneEntry]]` — Contact phone numbers displayed on the agent's profile. At least 1 and up to 3 entries.
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[AgentEmailEntry]]` — Contact email addresses displayed on the agent's profile. At least 1 and up to 3 entries.
    
</dd>
</dl>

<dl>
<dd>

**websites:** `typing.Optional[typing.Sequence[AgentWebsiteEntry]]` — Website links displayed on the agent's profile. At least 1 and up to 3 entries.
    
</dd>
</dl>

<dl>
<dd>

**privacy_url:** `typing.Optional[str]` — URL to the agent's privacy policy.
    
</dd>
</dl>

<dl>
<dd>

**terms_url:** `typing.Optional[str]` — URL to the agent's terms and conditions.
    
</dd>
</dl>

<dl>
<dd>

**color:** `typing.Optional[str]` — The agent's brand color as a hex color code. Must have sufficient contrast with white.
    
</dd>
</dl>

<dl>
<dd>

**is_conversational:** `typing.Optional[bool]` — Whether the agent supports two-way conversations.
    
</dd>
</dl>

<dl>
<dd>

**agent_use_case:** `typing.Optional[AgentUseCase]` 
    
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

<details><summary><code>client.rcs.test.<a href="src/rcs/rcs/test/client.py">whitelist_number</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Whitelist a phone number for testing with a specific test agent.

During development and testing, RCS agents can only send messages to whitelisted phone numbers.
Use this endpoint to whitelist specific phone numbers so you can send and receive messages from the test agent.

## Verification Process

After whitelisting, the recipient must accept the tester invite:

1. The recipient's device will receive a message from "RBM Tester Management".
2. The recipient must tap "Make me a tester" to accept.
3. Once accepted, the status transitions from `PENDING` to `ACCEPTED`.

## Verification

<div style="display: flex; gap: 16px;">
  <div style="flex: 1; text-align: center;">
    <strong>Accepting the invite</strong><br/>
    <img src="https://pncl.to/f769cAvCbEx-MmezZjR6dz6KVkr5ZO" alt="Accepting the tester invite" style="max-width: 100%;" />
  </div>
  <div style="flex: 1; text-align: center;">
    <strong>Declining the invite</strong><br/>
    <img src="https://pncl.to/VRere3tEKfx4n0HNaxK-vwl7pbLHTJ" alt="Declining the tester invite" style="max-width: 100%;" />
  </div>
</div>

## Cooldown

There is a **2-minute cooldown** after creating or updating a test agent before you can whitelist numbers.
Attempting to whitelist during the cooldown returns a `500` error with the remaining wait time.
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
client.rcs.test.whitelist_number(
    agent_id="agent_abc123def456",
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

**agent_id:** `str` — The RCS agent ID (must be prefixed with `agent_`).
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `str` — Phone number to whitelist for testing in E.164 format.
    
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

<details><summary><code>client.rcs.test.<a href="src/rcs/rcs/test/client.py">get_whitelist_status</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check the current whitelist status of a phone number for a specific test agent.

Use this endpoint to poll the status of a previously whitelisted number and determine
whether the recipient has accepted or rejected the tester invite.

## Status Values

- **`PENDING`** — The tester invite was sent but the recipient has not yet responded. Ask the recipient to check their messages and accept the invite.
- **`ACCEPTED`** — The recipient accepted the invite. Messages can be exchanged.
- **`REJECTED`** — The recipient rejected the invite or the invite could not be delivered since the carrier does not support test agents. If the user rejected the invite, they can accept it again by tapping "Make me a tester" in the same message from "RBM Tester Management".

<div style="display: flex; gap: 16px;">
  <div style="flex: 1; text-align: center;">
    <strong>Accepting the invite</strong><br/>
    <img src="https://pncl.to/f769cAvCbEx-MmezZjR6dz6KVkr5ZO" alt="Accepting the tester invite" style="max-width: 100%;" />
  </div>
  <div style="flex: 1; text-align: center;">
    <strong>Declining the invite</strong><br/>
    <img src="https://pncl.to/VRere3tEKfx4n0HNaxK-vwl7pbLHTJ" alt="Declining the tester invite" style="max-width: 100%;" />
  </div>
</div>
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
client.rcs.test.get_whitelist_status(
    agent_id="agent_abc123def456",
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

**agent_id:** `str` — The RCS agent ID (must be prefixed with `agent_`).
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `str` — The phone number to check whitelist status for (E.164 format).
    
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

<details><summary><code>client.tools.url.<a href="src/rcs/tools/url/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all shortened URLs with pagination. Results are sorted by creation date, newest first.
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
client.tools.url.list()

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

**page_index:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint:** `typing.Optional[str]` — Case-insensitive substring search on the destination URL.
    
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

