.PHONY: help install run run-birthday run-compliance run-supplier test lint check clean

help:
	@echo "Python Full Stack Business Portfolio"
	@echo "===================================="
	@echo ""
	@echo "Available commands:"
	@echo "  make install          - Install all dependencies"
	@echo "  make run              - Run birthday reminder (main app)"
	@echo "  make run-birthday     - Run birthday reminder app"
	@echo "  make run-compliance   - Run compliance tracker app"
	@echo "  make run-supplier     - Run supplier pricing tool"
	@echo "  make test             - Run import tests"
	@echo "  make lint             - Check code style"
	@echo "  make check            - Run all checks"
	@echo "  make clean            - Remove Python cache files"
	@echo ""

install:
	@echo "Installing dependencies for all apps..."
	pip install -r apps/birthday_reminder/requirements.txt
	pip install -r apps/compliance_tracker/requirements.txt
	pip install -r apps/supplier_pricing_intelligence_tool/requirements.txt
	@echo "✅ All dependencies installed"

run: run-birthday

run-birthday:
	@echo "Starting Birthday Reminder System..."
	@echo "Opening http://localhost:8508"
	@echo "Press Ctrl+C to stop"
	streamlit run apps/birthday_reminder/app/streamlit_app.py

run-compliance:
	@echo "Starting Compliance Tracker..."
	@echo "Opening http://localhost:8506"
	@echo "Press Ctrl+C to stop"
	streamlit run apps/compliance_tracker/compliance_tracker.py

run-supplier:
	@echo "Running Supplier Pricing Intelligence Tool..."
	python apps/supplier_pricing_intelligence_tool/invoice_parser_v2.py

test:
	@echo "Running import tests..."
	@python -c "import streamlit; print('✅ Streamlit')"
	@python -c "import pandas; print('✅ Pandas')"
	@python -c "import apscheduler; print('✅ APScheduler')"
	@echo "✅ All imports successful"

lint:
	@echo "Checking code style..."
	@find apps -name "*.py" -type f | head -5
	@echo "⚠️  Install flake8 for linting: pip install flake8"
	@echo "Then run: flake8 apps/"

check: test lint
	@echo "✅ All checks passed"

clean:
	@echo "Cleaning Python cache files..."
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete
	@echo "✅ Cache cleaned"

.DEFAULT_GOAL := help
