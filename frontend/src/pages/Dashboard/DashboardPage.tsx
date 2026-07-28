const DashboardPage = () => {
  return (
    <div className="flex h-screen bg-gray-950 text-white">
      {/* Sidebar */}
      <aside className="w-72 border-r border-gray-800">
        Sidebar
      </aside>

      {/* Chat */}
      <main className="flex flex-1 items-center justify-center">
        Chat Window
      </main>

      {/* Documents */}
      <aside className="w-80 border-l border-gray-800">
        Documents
      </aside>
    </div>
  );
};

export default DashboardPage;