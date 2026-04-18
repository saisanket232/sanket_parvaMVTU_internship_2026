import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";

function EditEmployee() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: "", email: "", phone: "",
    department: "", salary: "", joined_date: "",
  });
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/employee_app/api/employees/${id}/`)
      .then((res) => res.json())
      .then((data) => setFormData(data))
      .catch(() => setMessage("Failed to load employee data"));
  }, [id]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch(`http://127.0.0.1:8000/employee_app/api/employees/${id}/`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    })
      .then((res) => {
        if (!res.ok) throw new Error("Update failed");
        return res.json();
      })
      .then(() => navigate("/"))
      .catch(() => setMessage("Error updating employee"));
  };

  const initials = formData.name
    ? formData.name.slice(0, 2).toUpperCase()
    : "??";

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
      background: "#eff6ff",
      color: "#2563eb",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      fontWeight: 600,
      fontSize: 16,
      flexShrink: 0,
    },
    headerText: {
      flex: 1,
    },
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
      transition: "border-color 0.15s, background 0.15s",
    },
    actions: {
      display: "flex",
      gap: 10,
      paddingTop: 20,
      borderTop: "1px solid #f3f4f6",
    },
    saveBtn: {
      flex: 1,
      padding: "10px 0",
      background: "#2563eb",
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
  };

  return (
    <div style={styles.page}>
      <button style={styles.backBtn} onClick={() => navigate("/")}>
        ← Back to Employees
      </button>

      {message && <div style={styles.errorMsg}>{message}</div>}

      <div style={styles.card}>
        <div style={styles.header}>
          <div style={styles.avatar}>{initials}</div>
          <div style={styles.headerText}>
            <p style={styles.title}>{formData.name || "Employee"}</p>
            <p style={styles.subtitle}>Editing employee #{id}</p>
          </div>
        </div>

        <form onSubmit={handleSubmit}>
          <div style={styles.grid}>
            <div style={styles.fieldGroupFull}>
              <label style={styles.label}>Full Name</label>
              <input
                style={styles.input}
                name="name"
                value={formData.name}
                placeholder="Full name"
                onChange={handleChange}
              />
            </div>

            <div style={styles.fieldGroup}>
              <label style={styles.label}>Email</label>
              <input
                style={styles.input}
                name="email"
                value={formData.email}
                placeholder="Email address"
                onChange={handleChange}
              />
            </div>

            <div style={styles.fieldGroup}>
              <label style={styles.label}>Phone</label>
              <input
                style={styles.input}
                name="phone"
                value={formData.phone}
                placeholder="Phone number"
                onChange={handleChange}
              />
            </div>

            <div style={styles.fieldGroup}>
              <label style={styles.label}>Department</label>
              <input
                style={styles.input}
                name="department"
                value={formData.department}
                placeholder="Department"
                onChange={handleChange}
              />
            </div>

            <div style={styles.fieldGroup}>
              <label style={styles.label}>Salary</label>
              <input
                style={styles.input}
                name="salary"
                value={formData.salary}
                placeholder="Salary"
                onChange={handleChange}
              />
            </div>

            <div style={styles.fieldGroupFull}>
              <label style={styles.label}>Joined Date</label>
              <input
                style={styles.input}
                name="joined_date"
                value={formData.joined_date}
                type="date"
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
            <button type="submit" style={styles.saveBtn}>
              Save Changes
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default EditEmployee;