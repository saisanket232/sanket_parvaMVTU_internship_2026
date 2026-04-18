import React, { useEffect, useState } from "react";
import { Link, useLocation } from "react-router-dom";

function Employees() {
  const [employees, setEmployees] = useState([]);
  const location = useLocation();

  // ✅ Fetch employees
  useEffect(() => {
    fetch("http://127.0.0.1:8000/employee_app/api/employees/")
      .then((res) => res.json())
      .then((data) => setEmployees(data))
      .catch((err) => console.error(err));
  }, [location.key]);

  // ✅ DELETE FUNCTION (must be before return)
  const handleDelete = (id) => {
    if (!window.confirm("Are you sure you want to delete this employee?")) return;

    fetch(`http://127.0.0.1:8000/employee_app/api/employees/${id}/`, {
      method: "DELETE",
    })
      .then((res) => {
        if (res.ok) {
          // remove from UI instantly
          setEmployees((prev) => prev.filter((emp) => emp.id !== id));
        } else {
          console.error("Failed to delete");
        }
      })
      .catch((err) => console.error(err));
  };

  // ✅ UI
  return (
    <div style={{ padding: "20px", maxWidth: "600px", margin: "0 auto", fontFamily: "system-ui, -apple-system, sans-serif" }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
        <h1 style={{ margin: 0, fontSize: '24px', color: '#111827' }}>Employees</h1>
        <Link to="/register" style={{
          background: '#2563eb',
          color: 'white',
          textDecoration: 'none',
          padding: '8px 16px',
          borderRadius: '6px',
          fontWeight: 500,
          fontSize: '14px'
        }}>
          Add Employee
        </Link>
      </div>

      {employees.length === 0 ? (
        <p style={{ color: '#6b7280', textAlign: 'center', marginTop: '40px' }}>No employees found</p>
      ) : (
        employees.map((emp) => (
          <div
            key={emp.id}
            style={{
              background: 'white',
              border: '1px solid #e5e7eb',
              borderRadius: '12px',
              padding: '1.25rem',
              marginBottom: '1rem',
              boxShadow: '0 1px 2px 0 rgba(0, 0, 0, 0.05)'
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '14px' }}>
              <div style={{
                width: 44, height: 44, borderRadius: '50%',
                background: '#eff6ff', color: '#2563eb',
                display: 'flex', alignItems: 'center', justifyContent: 'center',
                fontWeight: 500, fontSize: 14
              }}>
                {emp.name ? emp.name.slice(0, 2).toUpperCase() : ""}
              </div>
              <div>
                <p style={{ fontWeight: 500, margin: 0, color: '#111827' }}>{emp.name}</p>
                <span style={{ display: 'inline-block', marginTop: '4px', fontSize: 12, background: '#f3f4f6', color: '#4b5563', padding: '2px 8px', borderRadius: 6 }}>
                  {emp.department}
                </span>
              </div>
            </div>
            
            {/* details grid */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px', marginBottom: '16px', fontSize: '14px', color: '#4b5563' }}>
              <div>
                <strong style={{ display: 'block', fontSize: '12px', color: '#9ca3af', marginBottom: '2px' }}>Email</strong>
                <span style={{ wordBreak: 'break-all' }}>{emp.email}</span>
              </div>
              <div>
                <strong style={{ display: 'block', fontSize: '12px', color: '#9ca3af', marginBottom: '2px' }}>Phone</strong>
                {emp.phone}
              </div>
              <div>
                <strong style={{ display: 'block', fontSize: '12px', color: '#9ca3af', marginBottom: '2px' }}>Salary</strong>
                ${emp.salary}
              </div>
              <div>
                <strong style={{ display: 'block', fontSize: '12px', color: '#9ca3af', marginBottom: '2px' }}>Joined Date</strong>
                {emp.joined_date}
              </div>
            </div>

            {/* action buttons */}
            <div style={{ display: 'flex', gap: '8px' }}>
              <Link to={`/edit/${emp.id}`} style={{
                textDecoration: 'none',
                flex: 1,
                textAlign: 'center',
                padding: '8px',
                borderRadius: '6px',
                fontWeight: 500,
                fontSize: '14px',
                color: '#2563eb',
                border: '1px solid #bfdbfe',
                background: 'white',
                cursor: 'pointer'
              }}>
                Edit
              </Link>
              <button onClick={() => handleDelete(emp.id)} style={{
                flex: 1,
                padding: '8px',
                borderRadius: '6px',
                fontWeight: 500,
                fontSize: '14px',
                color: '#dc2626',
                border: '1px solid #fecaca',
                background: 'white',
                cursor: 'pointer',
                fontFamily: 'inherit'
              }}>
                Delete
              </button>
            </div>
          </div>
        ))
      )}
    </div>
  );
}

export default Employees;