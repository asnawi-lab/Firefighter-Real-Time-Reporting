// react_component.tsx
import React from "react";

interface Incident {
  location: string;
  type: string;
  status: string;
}

const IncidentCard: React.FC<{ incident: Incident }> = ({ incident }) => {
  return (
    <div className="p-4 border rounded-xl shadow-md bg-white">
      <h2 className="text-lg font-bold">{incident.type}</h2>
      <p className="text-gray-600">📍 {incident.location}</p>
      <p
        className={`font-semibold ${
          incident.status === "Received" ? "text-green-600" : "text-yellow-600"
        }`}
      >
        Status: {incident.status}
      </p>
    </div>
  );
};

export default IncidentCard;
