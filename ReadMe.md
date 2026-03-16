AtlasCore – Multi-Tenant SaaS Platform

AtlasCore is a multi-tenant SaaS backend built with Django and PostgreSQL.
The platform is designed to support multiple organizations (tenants) within a single system while ensuring complete data isolation, secure authentication, and scalable architecture.

This project focuses on building a production-grade backend architecture similar to modern SaaS platforms such as Slack, Notion, or GitHub, where each company operates within its own isolated environment

Architecture Overview

AtlasCore uses a schema-based multi-tenancy model powered by django-tenants.
Each tenant (company) receives its own PostgreSQL schema while sharing the same application codebase.

This architecture provides:
	•	Strong data isolation
	•	Scalability for multiple organizations
	•	Simplified infrastructure management
	•	SaaS-ready backend design

Tech Stack

Backend Framework
	•	Django

API Layer
	•	Django REST Framework

Authentication
	•	JWT (SimpleJWT)

Database
	•	PostgreSQL

Multi-Tenancy
	•	django-tenants

Language
	•	Python

⸻

Key Features Implemented

Multi-Tenant Architecture

The system supports multiple tenants where each tenant operates within its own PostgreSQL schema.

Each tenant has:
	•	Isolated database schema
	•	Independent users
	•	Independent organizations
	•	Independent permissions and roles

⸻

Tenant Provisioning Service

A dedicated service layer automatically provisions new tenants.

Tenant provisioning includes:
	1.	Creating a new PostgreSQL schema
	2.	Registering the tenant domain
	3.	Running schema migrations
	4.	Creating the tenant administrator
	5.	Creating the default organization
	6.	Assigning the owner role

This allows new companies to be onboarded automatically.

⸻

JWT Authentication

Authentication is handled using JSON Web Tokens.

Endpoints:

POST /api/auth/login/
POST /api/auth/refresh/

The system returns:
	•	Access token
	•	Refresh token

These tokens allow secure API access across the platform.

⸻

User System

A custom Django user model is implemented.

Key features:
	•	Email-based authentication
	•	JWT authentication support
	•	Organization membership
	•	Role assignment

⸻

Organization System

Organizations represent teams within a tenant.

An organization includes:
	•	Owner
	•	Members
	•	Roles
	•	Invitations

This allows structured team management inside each tenant environment.

⸻

Role System

The platform implements a role-based access model.

Supported roles include:
	•	Owner
	•	Admin
	•	Member
	•	Auditor

Roles determine a user’s permissions within an organization.

⸻

User Invitation System

Organizations can invite users to join their workspace.

Invitation flow:
Admin invites user
        ↓
Invitation token generated
        ↓
User registers or logs in
        ↓
Invitation accepted
        ↓
Role assigned within organization

Invitations include:
	•	email
	•	organization
	•	role
	•	unique invitation token
	•	expiration date

⸻

Project Structure

atlascore/
│
├── accounts/
│   ├── models.py
│   ├── services/
│   │     └── invitations.py
│   └── api/
│
├── tenants/
│   ├── models.py
│   └── services/
│         └── provisioning.py
│
├── billing/
├── reports/
├── notifications/
├── security/
├── audit/
│
├── atlascore/
│   ├── settings.py
│   └── urls.py
│
└── manage.py

Running the Project

Clone the Repository

git clone https://github.com/OscarKingIn/atlascore.git

cd atlascore

Create Virtual Environment
python -m venv .venv
source .venv/bin/activate

Install Dependencies
pip install -r requirements.txt

Configure PostgreSQL

Update database configuration inside settings.py.

Example:
DATABASES = {
    "default": {
        "ENGINE": "django_tenants.postgresql_backend",
        "NAME": "atlascore",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

Run Migrations
python manage.py makemigrations
python manage.py migrate_schemas

Run the Development Server
python manage.py runserver

Current Development Stage

The project currently supports:
	•	Multi-tenant SaaS architecture
	•	Tenant provisioning service
	•	JWT authentication
	•	Custom user model
	•	Organization management
	•	Role system
	•	Invitation system

⸻

Planned Features

Upcoming features include:
	•	Permission-based RBAC
	•	Organization member management APIs
	•	Billing and subscription system
	•	Audit logging
	•	Security monitoring
	•	Notification service
	•	Admin dashboards
	•	React frontend integration

⸻

Goal of the Project

The goal of AtlasCore is to build a scalable SaaS platform architecture that demonstrates production-ready backend engineering practices including:
	•	multi-tenancy
	•	service-layer architecture
	•	role-based access control
	•	secure authentication
	•	modular system design

This project serves as both a learning platform and a demonstration of backend system architecture.
