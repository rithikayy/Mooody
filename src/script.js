class JournalApp {
  constructor() {
    this.form = document.getElementById("journal-form")
    this.entriesContainer = document.getElementById("entries")
    this.clearAllBtn = document.getElementById("clear-all")
    this.entries = this.loadEntries()

    this.init()
  }

  init() {
    this.form.addEventListener("submit", (e) => this.handleSubmit(e))
    this.clearAllBtn.addEventListener("click", () => this.clearAllEntries())
    this.displayEntries()
  }

  handleSubmit(e) {
    e.preventDefault()

    const formData = new FormData(this.form)
    const moodRating = formData.get("scale")
    const journalText = formData.get("journalentry").trim()

    if (!moodRating) {
      this.showNotification("Please select a mood rating", "error")
      return
    }

    if (!journalText) {
      this.showNotification("Please write something in your journal", "error")
      return
    }

    const entry = {
      id: Date.now(),
      date: new Date().toISOString(),
      mood: Number.parseInt(moodRating),
      text: journalText,
      timestamp: Date.now(),
    }

    this.addEntry(entry)
    this.form.reset()
    this.showNotification("Journal entry saved successfully! 🐄", "success")
  }

  addEntry(entry) {
    this.entries.unshift(entry) // Add to beginning of array
    this.saveEntries()
    this.displayEntries()
  }

  displayEntries() {
    if (this.entries.length === 0) {
      this.entriesContainer.innerHTML = `
                <div class="no-entries">
                    <p>No entries yet. Start by sharing how you're feeling today! 💭</p>
                </div>
            `
      return
    }

    const entriesHTML = this.entries.map((entry) => this.createEntryHTML(entry)).join("")
    this.entriesContainer.innerHTML = entriesHTML
  }

  createEntryHTML(entry) {
    const date = new Date(entry.date)
    const formattedDate = date.toLocaleDateString("en-US", {
      weekday: "long",
      year: "numeric",
      month: "long",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    })

    const moodClass = this.getMoodClass(entry.mood)
    const moodEmoji = this.getMoodEmoji(entry.mood)

    return `
            <div class="entry" data-id="${entry.id}">
                <div class="entry-header">
                    <span class="entry-date">${formattedDate}</span>
                    <span class="mood-badge ${moodClass}">
                        ${moodEmoji} Mood: ${entry.mood}/10
                    </span>
                </div>
                <div class="entry-text">${this.escapeHtml(entry.text)}</div>
            </div>
        `
  }

  getMoodClass(mood) {
    if (mood <= 3) return "mood-low"
    if (mood <= 7) return "mood-medium"
    return "mood-high"
  }

  getMoodEmoji(mood) {
    if (mood <= 2) return "😢"
    if (mood <= 4) return "😔"
    if (mood <= 6) return "😐"
    if (mood <= 8) return "🙂"
    return "😊"
  }

  escapeHtml(text) {
    const div = document.createElement("div")
    div.textContent = text
    return div.innerHTML
  }

  clearAllEntries() {
    if (this.entries.length === 0) {
      this.showNotification("No entries to clear", "info")
      return
    }

    if (confirm("Are you sure you want to delete all journal entries? This action cannot be undone.")) {
      this.entries = []
      this.saveEntries()
      this.displayEntries()
      this.showNotification("All entries have been cleared", "success")
    }
  }

  loadEntries() {
    try {
      const stored = localStorage.getItem("journalEntries")
      return stored ? JSON.parse(stored) : []
    } catch (error) {
      console.error("Error loading entries:", error)
      return []
    }
  }

  saveEntries() {
    try {
      localStorage.setItem("journalEntries", JSON.stringify(this.entries))
    } catch (error) {
      console.error("Error saving entries:", error)
      this.showNotification("Error saving entry. Please try again.", "error")
    }
  }

  showNotification(message, type = "info") {

    const existingNotification = document.querySelector(".notification")
    if (existingNotification) {
      existingNotification.remove()
    }

    const notification = document.createElement("div")
    notification.className = `notification notification-${type}`
    notification.textContent = message

    // Add styles
    Object.assign(notification.style, {
      position: "fixed",
      top: "20px",
      right: "20px",
      padding: "1rem 1.5rem",
      borderRadius: "8px",
      color: "white",
      fontWeight: "500",
      zIndex: "1000",
      transform: "translateX(100%)",
      transition: "transform 0.3s ease",
      maxWidth: "300px",
      wordWrap: "break-word",
    })

 
    const colors = {
      success: "#48bb78",
      error: "#f56565",
      info: "#4299e1",
    }
    notification.style.backgroundColor = colors[type] || colors.info

    document.body.appendChild(notification)


    setTimeout(() => {
      notification.style.transform = "translateX(0)"
    }, 100)


    setTimeout(() => {
      notification.style.transform = "translateX(100%)"
      setTimeout(() => {
        if (notification.parentNode) {
          notification.remove()
        }
      }, 300)
    }, 3000)
  }

 
  exportToCSV() {
    if (this.entries.length === 0) {
      this.showNotification("No entries to export", "info")
      return
    }

    const headers = ["Date", "Mood Rating", "Journal Entry"]
    const csvContent = [
      headers.join(","),
      ...this.entries.map((entry) =>
        [new Date(entry.date).toISOString(), entry.mood, `"${entry.text.replace(/"/g, '""')}"`].join(","),
      ),
    ].join("\n")

    const blob = new Blob([csvContent], { type: "text/csv" })
    const url = window.URL.createObjectURL(blob)
    const a = document.createElement("a")
    a.href = url
    a.download = `journal-entries-${new Date().toISOString().split("T")[0]}.csv`
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    window.URL.revokeObjectURL(url)

    this.showNotification("Entries exported successfully!", "success")
  }
}


document.addEventListener("DOMContentLoaded", () => {
  new JournalApp()
})


document.addEventListener("keydown", (e) => {

  if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
    const form = document.getElementById("journal-form")
    if (form) {
      form.dispatchEvent(new Event("submit"))
    }
  }
})
