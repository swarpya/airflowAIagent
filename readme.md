Here’s your complete `README.md` for a manual Apache Airflow 3.x installation (simple mode) in GitHub Codespaces or any local dev setup:

```markdown
# Apache Airflow 3.x: Quick Manual Setup (Simple Mode)

A step-by-step guide to manually install and run Apache Airflow 3.x for fast development in GitHub Codespaces or local environments, using the default “simple mode” (SimpleAuthManager). This guide includes all environment, configuration, and permission commands.

---

## 1. Create and Activate Python Virtual Environment

```
python3 -m venv .venv
source .venv/bin/activate
```

---

## 2. Set AIRFLOW_HOME

By default, Airflow uses `~/airflow`, but to keep your setup tidy (especially in Codespaces):

```
export AIRFLOW_HOME=$(pwd)/airflow_home
mkdir -p $AIRFLOW_HOME
```
Add the `export` line to your `.bashrc` or `.zshrc` to make it persistent.

---

## 3. Install Apache Airflow

Replace `3.12` with your Python version if different:

```
pip install "apache-airflow==3.0.6" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.6/constraints-3.12.txt"
```

---

## 4. Set File and Directory Permissions

Fix permissions so Airflow can read and write metadata/log files:

```
chmod -R 755 $AIRFLOW_HOME
```

---

## 5. Initialize Airflow Database

> Airflow 3.x: **`airflow db init` is deprecated/removed**
> Now use:

```
airflow db migrate
```

---

## 6. Start Airflow (Development Mode)

> Don’t use `airflow webserver`/`scheduler` in v3.x.
> Launch everything in one dev command:

```
airflow standalone
```
Wait for Airflow to print UI URL and login info.

---

## 7. Access the Airflow UI

- In Codespaces: Forward port 8080 and open the provided URL.
- In local: Browse to `http://localhost:8080`.

**Login:**  
If prompted, use credentials shown in your terminal. In simple mode, any username/password often works—all users are admins.

---

## 8. Troubleshooting: “Forbidden” or Permission Errors

- Double-check `$AIRFLOW_HOME` permissions:
  ```
  chmod -R 755 $AIRFLOW_HOME
  ```
- Make sure you start Airflow from your project’s root directory.
- Ensure port 8080 is forwarded and visible.
- Try incognito mode if the browser caches errors.

---

## Notes

- In simple mode, **user creation commands (`airflow users create`) are not needed or available**.
- For production or RBAC, see Airflow docs on enabling the FAB Auth Manager and secure authentication.
- This guide is intended for fast prototyping, demos, and initial experimentation.

---

**Enjoy your Airflow journey!**
```

Copy and place this content in your project as `README.md`—it contains every step, required change, and relevant command for a successful developer install.