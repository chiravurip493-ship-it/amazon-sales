# To-Do List Application

A modern, feature-rich to-do list application with persistent local storage functionality.

## Features

✨ **Core Features:**
- ✅ Add, edit, and delete tasks
- ✅ Mark tasks as completed
- ✅ Filter tasks (All, Active, Completed)
- ✅ Set priority levels for tasks
- ✅ Real-time statistics (Total, Active, Completed)
- ✅ Beautiful, responsive UI

💾 **Storage:**
- ✅ Persistent local storage using browser's localStorage API
- ✅ Automatic saving of all changes
- ✅ Data persists across browser sessions

📊 **User Interface:**
- ✅ Modern gradient design
- ✅ Smooth animations and transitions
- ✅ Mobile-responsive layout
- ✅ Dark mode compatible
- ✅ Intuitive controls

## How to Use

### Getting Started

1. Open `index.html` in your web browser
2. Start adding tasks immediately!

### Adding Tasks

1. Type your task in the input field
2. Click "Add" button or press Enter
3. Your task appears in the list

### Managing Tasks

- **Complete a Task**: Click the checkbox next to the task
- **Edit a Task**: Click the "Edit" button to modify the task text
- **Delete a Task**: Click the "Delete" button to remove a task
- **Set Priority**: Choose from High, Medium, or Low priority levels

### Filtering Tasks

Use the filter buttons to view:
- **All**: Show all tasks
- **Active**: Show only incomplete tasks
- **Completed**: Show only completed tasks

### Clearing Tasks

- **Clear Completed**: Remove all completed tasks at once
- **Clear All**: Remove all tasks (with confirmation)

## File Structure

```
todo-app/
├── index.html        # HTML structure
├── styles.css        # Styling and animations
├── app.js            # Application logic
└── README.md         # Documentation
```

## Technical Details

### Local Storage

The application uses the browser's `localStorage` API to persist data:

```javascript
// Save todos
localStorage.setItem('todos', JSON.stringify(this.todos));

// Load todos
const stored = localStorage.getItem('todos');
this.todos = JSON.parse(stored);
```

### Data Structure

Each todo item contains:

```javascript
{
    id: 1234567890,           // Unique identifier (timestamp)
    text: "Task description", // The task text
    completed: false,         // Completion status
    priority: 'medium',       // Priority: 'high', 'medium', 'low'
    createdAt: "6/29/2026"   // Creation timestamp
}
```

### Browser Compatibility

- Chrome 4+
- Firefox 3.5+
- Safari 4+
- Edge (all versions)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Storage Limits

- **localStorage limit**: ~5-10MB per domain (varies by browser)
- The app can handle 1000+ tasks without issues
- Older browsers have lower limits (check your browser specifications)

## Privacy

- All data is stored locally on your device
- No data is sent to any server
- No external API calls
- Your tasks are completely private

## Tips for Best Experience

1. **Use meaningful task descriptions** - Short, clear descriptions help you stay organized
2. **Organize with priorities** - Use priority levels to focus on important tasks
3. **Regular maintenance** - Clear completed tasks to keep your list organized
4. **Backup your data** - Export tasks periodically (you can add this feature)

## Keyboard Shortcuts

- **Enter** - Add a new task (when input is focused)
- **Tab** - Navigate between filter buttons
- **Space** - Toggle checkbox

## Future Enhancements

Potential features for future versions:
- [ ] Due dates and reminders
- [ ] Task categories/tags
- [ ] Export/Import functionality
- [ ] Dark mode toggle
- [ ] Recurring tasks
- [ ] Notes/descriptions
- [ ] Local backup/restore
- [ ] Sound notifications

## Troubleshooting

### Tasks not saving?
- Check if localStorage is enabled in your browser
- Some browsers disable localStorage in private/incognito mode
- Clear browser cache and reload

### Tasks disappeared?
- Check if localStorage was cleared
- Try a different browser to see if data is browser-specific
- Check browser developer tools (F12) > Application > Local Storage

### Performance issues?
- If you have 1000+ tasks, consider archiving old ones
- Try clearing completed tasks to reduce list size

## License

This project is open source and available for personal and commercial use.

## Support

For issues, questions, or suggestions, please create an issue or contact the developer.

---

**Version**: 1.0.0  
**Last Updated**: June 2026  
**Author**: To-Do App Team
