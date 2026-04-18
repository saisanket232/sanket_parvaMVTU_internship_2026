import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function Register() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    department: "",
    salary: "",
    joined_date: "",
  });

  const [message, setMessage] = useState("");
  const [success, setSuccess] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("http://127.0.0.1:8000/employee_app/api/employees/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    })
      .then((res) => {
        if (!res.ok) throw new Error("Failed to register");
        return res.json();
      })
      .then(() => {
        setSuccess(true);
        setMessage("Employee registered successfully!");
        setTimeout(() => {
          window.location.href = "/";
        }, 1200);
      })
      .catch(() => {
        setSuccess(false);
        setMessage("Error registering employee. Please try again.");
      });
  };

  const initials = formData.name
    ? formData.name.slice(0, 2).toUpperCase()
    : "+";

  const styles = {
    page: {
      padding: "32px 20px",
      maxWidth: 520,
      margin: "0 auto",
      fontFamily: "'Segoe UI', sans-serif",
    },
    backBtn: {
      background: "none",
      border: "none",
      color: "#6b7280",
      fontSize: 14,
      cursor: "pointer",
      padding: "0 0 16px 0",
      display: "flex",
      alignItems: "center",
      gap: 6,
    },
    card: {
      background: "white",
      border: "1px solid #e5e7eb",
      borderRadius: 16,
      padding: "1.5rem",
      boxShadow: "0 1px 4px rgba(0,0,0,0.06)",
    },
    header: {
      display: "flex",
      alignItems: "center",
      gap: 14,
      marginBottom: 24,
      paddingBottom: 20,
      borderBottom: "1px solid #f3f4f6",
    },
    avatar: {
      width: 52,
      height: 52,
      borderRadius: "50%",
      background: "#f0fdf4",
      color: "#16a34a",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      fontWeight: 600,
      fontSize: 20,
      flexShrink: 0,
      border: "2px dashed #bbf7d0",
    },
    headerText: { flex: 1 },
    title: {
      fontSize: 18,
      fontWeight: 600,
      color: "#111827",
      margin: 0,
    },
    subtitle: {
      fontSize: 13,
      color: "#6b7280",
      margin: "2px 0 0",
    },
    grid: {
      display: "grid",
      gridTemplateColumns: "1fr 1fr",
      gap: "14px 16px",
      marginBottom: 20,
    },
    fieldGroup: {
      display: "flex",
      flexDirection: "column",
      gap: 5,
    },
    fieldGroupFull: {
      display: "flex",
      flexDirection: "column",
      gap: 5,
      gridColumn: "1 / -1",
    },
    label: {
      fontSize: 11,
      fontWeight: 600,
      color: "#9ca3af",
      textTransform: "uppercase",
      letterSpacing: "0.05em",
    },
    input: {
      padding: "9px 12px",
      border: "1px solid #e5e7eb",
      borderRadius: 8,
      fontSize: 14,
      color: "#111827",
      background: "#fafafa",
      outline: "none",
    },
    actions: {
      display: "flex",
      gap: 10,
      paddingTop: 20,
      borderTop: "1px solid #f3f4f6",
    },
    submitBtn: {
      flex: 1,
      padding: "10px 0",
      background: "#16a34a",
      color: "white",
      border: "none",
      borderRadius: 8,
      fontSize: 14,
      fontWeight: 600,
      cursor: "pointer",
    },
    cancelBtn: {
      flex: 1,
      padding: "10px 0",
      background: "white",
      color: "#374151",
      border: "1px solid #e5e7eb",
      borderRadius: 8,
      fontSize: 14,
      fontWeight: 500,
      cursor: "pointer",
    },
    errorMsg: {
      background: "#fef2f2",
      color: "#b91c1c",
      border: "1px solid #fecaca",
      borderRadius: 8,
      padding: "10px 14px",
      fontSize: 13,
      marginBottom: 16,
    },
    successMsg: {
      background: "#f0fdf4",
      color: "#15803d",
      border: "1px solid #bbf7d0",
      borderRadius: 8,
      padding: "10px 14px",
      fontSize: 13,
      marginBottom: 16,
    },
  };

  return (
    <div style={styles.page}>
      <button style={styles.backBtn} onClick={() => navigate("/")}>
        ← Back to Employees
      </button>

      {message && (
        <div style={success ? styles.successMsg : styles.errorMsg}>
          {message}
        </div>
      )}

      <div style={styles.card}>
        <div style={styles.header}>
          <div style={styles.avatar}>{initials}</div>
          <div style={styles.headerText}>
            <p style={styles.title}>
              {formData.name || "New Employee"}
            </p>
            <p style={styles.subtitle}>Fill in the details below to register</p>
          </div>
        </div>

        <form onSubmit={handleSubmit}>
          <div style={styles.grid}>
            <div style={styles.fieldGroupFull}>
              <label style={styles.label}>Full Name</label>
              <input
                style={styles.input}
                name="name"
                placeholder="Full name"
                value={formData.name}
                onChange={handleChange}
                required
              />
            </div>

            <div style={styles.fieldGroup}>
              <label style={styles.label}>Email</label>
              <input
                style={styles.input}
                name="email"
                placeholder="Email address"
                value={formData.email}
                onChange={handleChange}
                required
              />
            </div>

            <div style={styles.fieldGroup}>
              <label style={styles.label}>Phone</label>
              <input
                style={styles.input}
                name="phone"
                placeholder="Phone number"
                value={formData.phone}
                onChange={handleChange}
              />
            </div>

            <div style={styles.fieldGroup}>
              <label style={styles.label}>Department</label>
              <input
                style={styles.input}
                name="department"
                placeholder="Department"
                value={formData.department}
                onChange={handleChange}
              />
            </div>

            <div style={styles.fieldGroup}>
              <label style={styles.label}>Salary</label>
              <input
                style={styles.input}
                name="salary"
                placeholder="Salary"
                value={formData.salary}
                onChange={handleChange}
              />
            </div>

            <div style={styles.fieldGroupFull}>
              <label style={styles.label}>Joined Date</label>
              <input
                style={styles.input}
                name="joined_date"
                type="date"
                value={formData.joined_date}
                onChange={handleChange}
              />
            </div>
          </div>

          <div style={styles.actions}>
            <button
              type="button"
              style={styles.cancelBtn}
              onClick={() => navigate("/")}
            >
              Cancel
            </button>
            <button type="submit" style={styles.submitBtn}>
              Register Employee
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Register;