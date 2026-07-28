import { loginUser } from "../../services/authService";

const LoginPage = () => {
  const handleTest = async () => {
    try {
      const response = await loginUser({
        email: "suraj2@example.com",
        password: "password123",
      });

      console.log(response);
      alert("Backend Connected Successfully!");
    } catch (error) {
      console.error(error);
      alert("Backend Connection Failed");
    }
  };

  return (
    <div className="flex min-h-screen items-center justify-center">
      <button
        onClick={handleTest}
        className="rounded bg-blue-600 px-6 py-3 text-white"
      >
        Test Backend Connection
      </button>
    </div>
  );
};

export default LoginPage;