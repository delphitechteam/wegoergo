# Contact Form Specifications
**Complete Contact Page Design & Form Configuration for Squarespace**

---

## Contact Page Goal

**Primary:** Capture leads from visitors ready to schedule consultations or request quotes
**Secondary:** Provide easy ways to reach WegoErgo (phone, email, location)

**Key Strategy:** Make it EASY to contact you with multiple options and a simple form

---

## PAGE LAYOUT

### Overall Structure

```
┌────────────────────────────────────────────────────────────┐
│                    CONTACT PAGE                            │
│                                                            │
│  ┌──────────────────────────────────────────────┐         │
│  │             PAGE HEADER                       │         │
│  │  Let's Create a Healthier Workspace Together  │         │
│  └──────────────────────────────────────────────┘         │
│                                                            │
│  ┌─────────────────────┬──────────────────────┐          │
│  │  CONTACT FORM       │  CONTACT INFO        │          │
│  │  (60% width)        │  (40% width)         │          │
│  │                     │                      │          │
│  │  [Form fields...]   │  📞 Phone            │          │
│  │                     │  ✉️ Email            │          │
│  │                     │  📍 Location         │          │
│  │                     │  🕐 Hours            │          │
│  │                     │                      │          │
│  │  [Submit Button]    │  [Map/Image]         │          │
│  └─────────────────────┴──────────────────────┘          │
│                                                            │
│  ┌──────────────────────────────────────────────┐         │
│  │          WHAT HAPPENS NEXT                    │         │
│  │  (Process timeline after form submission)     │         │
│  └──────────────────────────────────────────────┘         │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## SECTION 1: PAGE HEADER

### Content

**H1 HEADLINE:**
```
Let's Create a Healthier Workspace Together
```

**SUBHEADLINE:**
```
Whether you need an ergonomic assessment, workspace design, or help
selecting the perfect furniture, we're here to help. Reach out today
and let's discuss your project.
```

**Design:**
- Centered text
- Clean, professional
- Ample white space
- Desktop: 60% width centered
- Mobile: 90% width

---

## SECTION 2: CONTACT FORM

### Form Layout (Left Column - 60%)

```
┌─────────────────────────────────────────┐
│  YOUR INFORMATION                       │
│                                         │
│  First Name *       Last Name *        │
│  [            ]     [            ]      │
│                                         │
│  Email Address *                        │
│  [                              ]       │
│                                         │
│  Phone Number *                         │
│  [                              ]       │
│                                         │
│  Company Name                           │
│  [                              ]       │
│                                         │
│  Industry (dropdown) *                  │
│  [Select Industry          ▼]          │
│                                         │
│  I'm Interested In (dropdown) *         │
│  [Select Service           ▼]          │
│                                         │
│  Tell Us About Your Project *           │
│  [                              ]       │
│  [                              ]       │
│  [                              ]       │
│  (multiline text area)                  │
│                                         │
│  How Did You Hear About Us? (optional)  │
│  [Select                   ▼]          │
│                                         │
│  [ ] Subscribe to newsletter           │
│                                         │
│  [     Send Message     ]              │
│  (submit button)                        │
│                                         │
└─────────────────────────────────────────┘
```

---

### FORM FIELDS - DETAILED SPECIFICATIONS

#### Field 1 & 2: Name (Side by Side)

**First Name**
- Field type: Text input
- Required: Yes (*)
- Placeholder: "John"
- Validation: Letters only, min 2 characters
- Error message: "Please enter your first name"

**Last Name**
- Field type: Text input
- Required: Yes (*)
- Placeholder: "Smith"
- Validation: Letters only, min 2 characters
- Error message: "Please enter your last name"

**Layout:** Two columns on desktop, stack on mobile

---

#### Field 3: Email Address

**Email Address**
- Field type: Email input
- Required: Yes (*)
- Placeholder: "you@company.com"
- Validation: Valid email format (contains @ and .)
- Error message: "Please enter a valid email address"

---

#### Field 4: Phone Number

**Phone Number**
- Field type: Tel input
- Required: Yes (*)
- Placeholder: "(555) 123-4567"
- Validation: Phone number format (allow various formats)
- Error message: "Please enter a valid phone number"
- Auto-formatting: Apply (XXX) XXX-XXXX format if possible

---

#### Field 5: Company Name

**Company Name**
- Field type: Text input
- Required: No
- Placeholder: "Your Company Name"
- Validation: None (optional field)

---

#### Field 6: Industry (Dropdown)

**Industry**
- Field type: Dropdown select
- Required: Yes (*)
- Default option: "Select Your Industry"

**Dropdown Options:**
```
Select Your Industry
─────────────────────
Healthcare
Corporate / Tech
Education
Government / Public Sector
Lab & Life Sciences
Small Business
Hospitality
Outdoor / Landscape
Other
```

**Error message:** "Please select your industry"

---

#### Field 7: Service Interest (Dropdown)

**I'm Interested In**
- Field type: Dropdown select
- Required: Yes (*)
- Default option: "Select a Service"

**Dropdown Options:**
```
Select a Service
─────────────────────────
Ergonomic Assessment
Workspace Design
Product Selection & Sourcing
Complete Turnkey Solution
Not Sure / Exploratory
```

**Error message:** "Please select a service"

---

#### Field 8: Project Details

**Tell Us About Your Project**
- Field type: Textarea (multiline)
- Required: Yes (*)
- Placeholder: "Please describe your workspace needs, challenges, or project details..."
- Rows: 5-6 lines visible
- Character limit: 1000 characters (optional)
- Validation: Minimum 20 characters
- Error message: "Please provide some details about your project (min 20 characters)"

---

#### Field 9: Referral Source (Optional)

**How Did You Hear About Us?**
- Field type: Dropdown select
- Required: No
- Default option: "Select an option"

**Dropdown Options:**
```
Select an option
─────────────────────────
Google Search
LinkedIn
Referral from Friend/Colleague
Industry Event
Social Media
Existing Client
Other
```

---

#### Field 10: Newsletter Opt-in

**Newsletter Subscription**
- Field type: Checkbox
- Required: No
- Label: "Yes, I'd like to receive ergonomic tips and product updates from WegoErgo"
- Default: Unchecked
- GDPR compliant: Must be opt-in, not pre-checked

---

### SUBMIT BUTTON

**Button Text:**
```
Send Message
```

**Alternative Options:**
- `Submit`
- `Contact WegoErgo`
- `Get In Touch`

**Button Styling:**
- Background: Primary brand color (#E67E50 orange)
- Text: White
- Size: Large (full width on mobile)
- Font weight: Semi-bold
- Padding: 14px vertical, 40px horizontal
- Border radius: 6px
- Hover: Darken slightly, lift effect

**Loading State:**
- Change button text to "Sending..." with spinner
- Disable button during submission

**Success State:**
- Show success message (see below)
- Clear form OR redirect to thank you page

---

### FORM VALIDATION

**Client-Side Validation (JavaScript):**
- Real-time validation as user types
- Show green checkmark for valid fields
- Show red error message for invalid fields
- Prevent submission if required fields missing

**Server-Side Validation:**
- Re-validate all fields on backend
- Sanitize inputs to prevent XSS
- Check for spam (honeypot field, reCAPTCHA optional)

**Error Handling:**
- Display errors below each field
- Scroll to first error on submit
- Keep user data in fields (don't clear on error)

---

### SPAM PROTECTION

**Recommended Methods:**

1. **Honeypot Field (Invisible):**
   - Add hidden field "website" or "url"
   - Hide with CSS (not display:none)
   - If filled, reject as spam
   - Best: invisible to users, effective against bots

2. **Google reCAPTCHA v3 (Optional):**
   - Invisible to users
   - Scores submissions 0-1
   - Reject scores below 0.5
   - Downside: Google branding, privacy concerns

3. **Time-Based Check:**
   - Track form load time
   - Reject if submitted in < 3 seconds
   - Humans can't fill form that fast

**Recommended: Use honeypot + time-based check** (no user friction)

---

## SECTION 3: CONTACT INFORMATION (Right Column - 40%)

### Layout

```
┌─────────────────────────────────┐
│   CONTACT INFORMATION           │
│                                 │
│   📞 PHONE                      │
│   (XXX) XXX-XXXX               │
│   [Call Now]                    │
│                                 │
│   ✉️ EMAIL                      │
│   info@wegoergo.com            │
│   [Email Us]                    │
│                                 │
│   📍 LOCATION                   │
│   Livermore Valley, CA          │
│   Serving the greater Bay Area │
│                                 │
│   🕐 HOURS                      │
│   Monday - Friday               │
│   8:00 AM - 5:00 PM PST        │
│   Weekends: By appointment      │
│                                 │
│   ─────────────────────────    │
│                                 │
│   [Map or Service Area Image]   │
│   or [Photo of Michael]         │
│                                 │
└─────────────────────────────────┘
```

### Content

**PHONE**
```
📞 PHONE
(925) XXX-XXXX
[Call Now]
```
- Make phone number clickable: `tel:+19255551234`
- Button opens phone dialer on mobile

**EMAIL**
```
✉️ EMAIL
info@wegoergo.com
[Email Us]
```
- Make email clickable: `mailto:info@wegoergo.com`
- Button opens email client

**LOCATION**
```
📍 LOCATION
Livermore Valley, California
Serving the greater Bay Area
```
- Optional: Add full address if you have physical location
- If no physical address, keep it regional

**HOURS**
```
🕐 BUSINESS HOURS
Monday - Friday
8:00 AM - 5:00 PM PST
Weekends: By appointment only
```

**VISUAL ELEMENT:**
- Map showing Bay Area coverage
- OR: Professional photo of Michael
- OR: Office/workspace photo
- Size: 300x300px minimum

---

### MOBILE LAYOUT FOR CONTACT INFO

**On Mobile:**
- Contact info section moves ABOVE form
- Shows as full-width cards
- Phone/Email buttons prominent
- Easy one-tap calling/emailing

---

## SECTION 4: WHAT HAPPENS NEXT

### Layout

```
┌────────────────────────────────────────────────────────────┐
│              WHAT HAPPENS NEXT?                            │
│                                                            │
│  After you submit your inquiry, here's what to expect:    │
│                                                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐ │
│  │    1️⃣    │  │    2️⃣    │  │    3️⃣    │  │    4️⃣    │ │
│  │          │  │          │  │          │  │          │ │
│  │We respond│  │Schedule  │  │Assess    │  │Recommend │ │
│  │within 24 │  │consult   │  │your needs│  │solutions │ │
│  │hours     │  │          │  │          │  │          │ │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘ │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### Content

**HEADLINE:**
```
What Happens Next?
```

**INTRO TEXT:**
```
After you submit your inquiry, here's what to expect:
```

**STEP 1:**
```
1️⃣ WE RESPOND WITHIN 24 HOURS
We'll reach out to confirm your inquiry and answer any initial questions.
```

**STEP 2:**
```
2️⃣ SCHEDULE A CONSULTATION
We'll set up a convenient time to discuss your workspace needs—in person
or virtually.
```

**STEP 3:**
```
3️⃣ ASSESS YOUR NEEDS
Michael conducts a thorough assessment of your workspace, workflow, and
ergonomic challenges.
```

**STEP 4:**
```
4️⃣ RECEIVE RECOMMENDATIONS
Get a detailed plan with tailored solutions, product recommendations, and
implementation support.
```

**Design:**
- 4 columns on desktop
- Stack vertically on mobile
- Icons or numbers for each step
- Light background to differentiate from main content

---

## FORM SUBMISSION HANDLING

### Success Message (Option 1: Inline)

**On Successful Submission, Replace Form With:**

```
┌─────────────────────────────────────────┐
│        ✅ MESSAGE SENT!                  │
│                                         │
│  Thank you for contacting WegoErgo!     │
│                                         │
│  We've received your message and will   │
│  respond within 24 hours. If you need   │
│  immediate assistance, feel free to     │
│  call us at (XXX) XXX-XXXX.            │
│                                         │
│  [Return to Homepage]                   │
│                                         │
└─────────────────────────────────────────┘
```

---

### Success Message (Option 2: Redirect to Thank You Page)

**Create separate "Thank You" page at `/thank-you`**

**Thank You Page Content:**
```
┌────────────────────────────────────────────────────────────┐
│                   ✅ THANK YOU!                             │
│                                                            │
│         Your message has been sent successfully            │
│                                                            │
│  We appreciate you reaching out to WegoErgo. Michael will │
│  personally review your inquiry and respond within 24     │
│  hours.                                                   │
│                                                            │
│  In the meantime, feel free to:                           │
│  • [Explore Our Services]                                 │
│  • [View Our Products]                                    │
│  • [Read About Michael]                                   │
│                                                            │
│  Need immediate help? Call (XXX) XXX-XXXX                 │
│                                                            │
│  [Return to Homepage]                                     │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

**Recommendation: Use inline success message** (keeps user on page, less disruptive)

---

### Error Message

**If Form Submission Fails:**

```
┌─────────────────────────────────────────┐
│  ❌ OOPS! SOMETHING WENT WRONG           │
│                                         │
│  We couldn't send your message. Please  │
│  try again or contact us directly:      │
│                                         │
│  Phone: (XXX) XXX-XXXX                 │
│  Email: info@wegoergo.com              │
│                                         │
│  [Try Again]                            │
│                                         │
└─────────────────────────────────────────┘
```

---

## EMAIL NOTIFICATIONS

### Admin Notification Email (to WegoErgo)

**Subject Line:**
```
New Contact Form Submission from [First Name] [Last Name]
```

**Email Body:**
```
New contact form submission received:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONTACT INFORMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Name: [First Name] [Last Name]
Email: [Email Address]
Phone: [Phone Number]
Company: [Company Name]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROJECT DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Industry: [Industry]
Service Interest: [Service]

Project Description:
[Message text]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ADDITIONAL INFO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Referral Source: [How they heard about you]
Newsletter Opt-in: [Yes/No]

Submitted: [Date/Time]
IP Address: [IP] (for spam tracking)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Reply to this inquiry]
```

---

### Auto-Reply Email (to User)

**Subject Line:**
```
Thanks for contacting WegoErgo!
```

**Email Body:**
```
Hi [First Name],

Thank you for reaching out to WegoErgo! We've received your message and
will respond within 24 hours.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOUR SUBMISSION DETAILS:

Industry: [Industry]
Service Interest: [Service]

Project Description:
[Their message]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

In the meantime, feel free to:

📞 Call us: (XXX) XXX-XXXX
✉️ Email: info@wegoergo.com
🌐 Visit our website: www.wegoergo.com

We look forward to helping you create a healthier, more productive workspace!

Best regards,
Michael Schiller
Founder & Certified Ergonomist
WegoErgo

──────────────────────────────────────
WegoErgo
Livermore Valley, CA
www.wegoergo.com
```

---

## SQUARESPACE FORM SETUP

### How to Build This Form in Squarespace

**Step-by-Step:**

1. **Add Form Block**
   - Go to Contact page
   - Add → Form

2. **Configure Fields**
   - Click "Edit" on form block
   - Add fields one by one:
     - Text fields (name, email, phone, company)
     - Dropdown fields (industry, service, referral)
     - Textarea (project details)
     - Checkbox (newsletter)

3. **Set Required Fields**
   - Toggle "Required" for: First Name, Last Name, Email, Phone, Industry, Service, Message
   - Leave Company, Referral, Newsletter as optional

4. **Configure Form Settings**
   - Storage: Squarespace stores submissions (downloadable)
   - Email Notifications:
     - Send to: info@wegoergo.com (or your email)
     - Subject: "New Contact Form Submission"
     - Auto-reply: Enable, customize message

5. **Customize Thank You Message**
   - Post-Submit: Show message OR redirect to thank you page
   - Message text (if inline): Use success message above

6. **Add Spam Protection**
   - Squarespace has built-in reCAPTCHA option
   - Enable in Form Settings → Storage → Enable reCAPTCHA

7. **Style the Form**
   - Use Squarespace's style editor
   - Match brand colors
   - Adjust spacing and fonts

---

## ACCESSIBILITY REQUIREMENTS

### Form Accessibility Checklist

✅ **All fields have labels** (not just placeholders)
✅ **Required fields marked with asterisk (*)**
✅ **Error messages are descriptive**
✅ **Form is keyboard navigable** (tab through fields)
✅ **Color contrast meets WCAG AA standards** (4.5:1 minimum)
✅ **Error states visible to screen readers**
✅ **Submit button has focus state**
✅ **Form validates before submission**

---

## MOBILE OPTIMIZATION

### Mobile Form Best Practices

**Field Inputs:**
- Full width on mobile
- Large touch targets (min 44px height)
- Appropriate keyboard types:
  - Email field → email keyboard
  - Phone field → number pad
  - Text field → standard keyboard

**Layout:**
- Stack all fields vertically
- Contact info moves above form
- Submit button full width
- Adequate spacing between fields

**Usability:**
- Auto-focus on first field (optional)
- Scroll to errors on validation failure
- Success message highly visible

---

## ANALYTICS & TRACKING

### Events to Track

**Google Analytics / Tag Manager:**

1. **Form Views**
   - Event: `form_view`
   - Track: Users who land on contact page

2. **Form Starts**
   - Event: `form_start`
   - Track: Users who interact with first field

3. **Form Submissions**
   - Event: `form_submit`
   - Track: Successful submissions
   - Parameters: industry, service_interest

4. **Form Errors**
   - Event: `form_error`
   - Track: Validation errors
   - Parameters: field_name, error_type

5. **Form Abandonment**
   - Event: `form_abandon`
   - Track: Users who start but don't submit

**Conversion Goal:**
- Set "Form Submission" as primary conversion goal
- Track conversion rate
- Monitor drop-off points

---

## GDPR & PRIVACY COMPLIANCE

### Required Privacy Elements

**Privacy Notice (below form):**
```
By submitting this form, you agree to our Privacy Policy. We will use
your information solely to respond to your inquiry and will not share
it with third parties.
```

**Link to Privacy Policy:**
- Create `/privacy-policy` page
- Link in footer
- Link near form submission

**Data Handling:**
- Store submissions securely
- Don't use data for marketing unless opted in
- Provide way to request data deletion (GDPR right to be forgotten)

---

## INTEGRATION OPTIONS

### Optional Integrations

**CRM Integration:**
- Connect to HubSpot, Salesforce, or Pipedrive
- Auto-create lead/contact on submission
- Track lead source

**Email Marketing:**
- If newsletter checkbox selected, add to email list
- Integrate with Mailchimp, ConvertKit, etc.
- Send welcome email

**Calendar Booking:**
- Add "Schedule Now" link to success message
- Integrate Calendly or similar
- Allow direct booking after form submission

**Slack/SMS Notifications:**
- Get instant alert on new submission
- Zapier integration for notifications

---

## TESTING CHECKLIST

### Before Launch, Test:

✅ All required fields validate correctly
✅ Email format validation works
✅ Phone format validation works
✅ Dropdown selections save correctly
✅ Textarea accepts sufficient characters
✅ Spam protection works (honeypot doesn't block real users)
✅ Submit button shows loading state
✅ Success message displays correctly
✅ Admin notification email arrives
✅ Auto-reply email arrives to user
✅ Mobile layout is usable
✅ Form is keyboard accessible
✅ Works in all major browsers (Chrome, Safari, Firefox, Edge)

---

## SAMPLE COMPLETED FORM DATA

### Example Submission

```
First Name: Jennifer
Last Name: Martinez
Email: jmartinez@healthcareclinic.com
Phone: (510) 555-1234
Company: Bay Area Health Clinic
Industry: Healthcare
I'm Interested In: Ergonomic Assessment
Message: We're renovating our nursing stations and need ergonomic
assessments for 30+ workstations. Looking for furniture recommendations
and installation coordination. Timeline: 3 months.
How Did You Hear About Us: Google Search
Newsletter: Yes (checked)
```

**This should generate:**
- Admin email to info@wegoergo.com
- Auto-reply to jmartinez@healthcareclinic.com
- Entry in Squarespace form submissions
- (Optional) CRM lead creation
- (Optional) Newsletter subscription

---

**This contact form is designed for maximum conversion with minimum friction. Simple, clear, and optimized for both desktop and mobile. You now have all 6 deliverables complete and ready to implement!**
