# Portfolio Website - Architecture Documentation

## Overview

This is a Flask-based portfolio website built for a creative graphic designer named Shishir Kandel. The application features a dynamic content management system with an admin panel for managing pages, contact forms, analytics tracking, and site configuration. The system is designed to be simple yet comprehensive, allowing for easy content updates and visitor interaction tracking.

## System Architecture

### Backend Architecture
- **Framework**: Flask web framework with modular blueprint structure
- **Database**: SQLAlchemy ORM with support for both SQLite (development) and PostgreSQL (production)
- **Authentication**: Flask-Login for admin session management
- **Forms**: WTForms with CSRF protection for secure form handling
- **Migrations**: Flask-Migrate for database schema versioning

### Frontend Architecture
- **Templates**: Jinja2 templating engine with base template inheritance
- **Styling**: Custom CSS with modern design principles and responsive layout
- **JavaScript**: Vanilla JavaScript for admin panel interactions
- **Rich Text Editor**: TinyMCE integration for content editing
- **UI Framework**: Bootstrap 5 for admin panel styling

## Key Components

### Models (models.py)
- **Admin**: User authentication model with password hashing
- **Page**: Dynamic content pages with SEO metadata and publishing controls
- **Contact**: Contact form submissions with read/unread status
- **Analytics**: Page view tracking with IP, user agent, and session data
- **SiteConfig**: Global site configuration settings

### Blueprints
- **Main Blueprint (views.py)**: Public-facing routes including homepage, dynamic pages, and contact form
- **Admin Blueprint (admin.py)**: Administrative interface for content management

### Forms (forms.py)
- **LoginForm**: Admin authentication
- **ContactForm**: Public contact submissions
- **PageForm**: Content creation and editing
- **SiteConfigForm**: Site-wide settings management

### Utilities (utils.py)
- **Analytics Tracking**: Automatic page view recording
- **Slug Generation**: URL-friendly slug creation from titles
- **Text Utilities**: Content truncation and formatting helpers

## Data Flow

### Public User Journey
1. Users visit the homepage displaying featured content and site configuration
2. Navigation allows access to dynamic pages created through admin
3. Contact form submissions are stored in database with automatic analytics tracking
4. All page views are anonymously tracked for analytics purposes

### Admin Workflow
1. Admin logs in through dedicated login page with session management
2. Dashboard provides overview statistics and recent activity
3. CRUD operations for pages with rich text editing capabilities
4. Contact message management with read/unread status tracking
5. Analytics viewing with time-based filtering
6. Site configuration management for global settings

### Database Interactions
- SQLAlchemy handles all database operations with connection pooling
- Automatic migration support for schema changes
- Optimized queries with relationship loading strategies

## External Dependencies

### Python Packages
- **Flask**: Core web framework (v3.1.1+)
- **Flask-SQLAlchemy**: Database ORM integration (v3.1.1+)
- **Flask-Login**: User session management
- **Flask-Migrate**: Database migration handling
- **Flask-WTF**: Form handling with CSRF protection
- **email-validator**: Email validation for contact forms (v2.2.0+)
- **psycopg2-binary**: PostgreSQL adapter for production (v2.9.10+)
- **gunicorn**: WSGI HTTP server for deployment (v23.0.0+)

### Frontend Libraries
- **Bootstrap 5**: CSS framework for admin interface
- **Font Awesome**: Icon library for UI elements
- **Google Fonts**: Inter font family for typography
- **TinyMCE**: Rich text editor for content management

### Development Tools
- **Nix**: Package management and development environment
- **PostgreSQL**: Production database system
- **OpenSSL**: Security libraries

## Deployment Strategy

### Production Configuration
- **Server**: Gunicorn WSGI server with autoscaling deployment target
- **Database**: PostgreSQL with connection pooling and automatic reconnection
- **Static Files**: Served through Flask with upload directory configuration
- **Security**: CSRF protection enabled, secure session management, proxy headers handling

### Environment Variables
- `DATABASE_URL`: Database connection string (auto-converts postgres:// to postgresql://)
- `SECRET_KEY`: Flask secret key for session signing
- `SESSION_SECRET`: Additional session security

### Deployment Features
- Automatic PostgreSQL URL format conversion for compatibility
- ProxyFix middleware for proper header handling behind reverse proxies
- Connection pooling with automatic reconnection for database reliability
- File upload limits (16MB) with dedicated upload directory

## Changelog
- June 19, 2025. Initial setup

## User Preferences

Preferred communication style: Simple, everyday language.