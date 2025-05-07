function sortMessages(messages) {
    const priorityMap = {
      urgent: 1,
      normal: 2,
      low: 3
    };
  
    return messages.sort((a, b) => {
      const priorityA = priorityMap[a.priority];
      const priorityB = priorityMap[b.priority];
  
      if (priorityA !== priorityB) {
        return priorityA - priorityB; // Higher priority first
      }
      return a.timestamp - b.timestamp; // FIFO within same priority
    });
  }
  